# 2 LoadingBar Documentation

### Creator: FlameChain

Github Link: [flamechain/Modules/](https://github.com/flamechain/Modules)

### Version: 1.1.7

Description: Extra documentation with larger and more specific examples. This mainly goes over how the [SimulateTasks()](./README.md#17-loadingbarsimulatetasks) method words, and how you can make it from scratch.

___

## 2.1 Contents

- [1.0 Main Documentation](./README.md) |
- [2.0 Secondary Documentation](#2-secondary-documentation)
- [2.1 Table of Contents](#21-contents)
- [2.2 Threading](#22-threading)
  - [2.2.1 threading.Thread](#221-threadingthread)
  - [2.2.2 concurrent.futures](#222-concurrentfutures)
- [2.3 Generating Tasks](#23-generating-tasks)
- [2.4 Other](#24-other)
- [2.5 Start() Method](#25-start)
- [2.6 End() Method](#26-end)
- [2.7 Conclusion](#27-cnclusion)

___

## 2.2 Threading

This section will mainly just go over how the [SimulateTasks()](./README.md#17-loadingbarsimulatetasks) class worked. You can always look at the code yourself [here](./loadingbar.py).

> Note: The [SimulateTasks()](./README.md#17-loadingbarsimulatetasks()) class is an example class without strict formatting, so it may be more difficult to read.

### 2.2.1 threading.Thread

In the [SimulateTasks()](./README.md#17-loadingbarsimulatetasks) class it uses the threading and concurrent modules. This section will go over just where it used the threading module to make it apear like its estimating eta without know how long the tasks will take.

```python
def runprogress(perc, done, stop):
    i = perc
    while True:
        if stop():
            break
        if i > 99:
            i = random.randint(75, 90)

        total_time = time.time() - start_time
        lb.progress(i, total_time, done)
        i += 1
```

First we make a function that just goes up by 1 percent every iteration. The base speed is initilized like so:

```python
start_time = time.time()
totaltime = time.time() - start_time

lb.progress(total, totaltime)
time.sleep(0.005*self.eta)
lb.progress(total+1, totaltime)
```

This code puts a 0.005*15 delay, or 0.075 second delay between 1 percent, telling the progress method that on average it should go up 13% per second. This was found to be a good baseline.

> Note: The 15 comes from the default eta parameter for the SimulateTasks() class.

The actaully threading comes in here. It runs the runprogress() method as 1 thread, and sleeps on the other, or the 'main' thread.

```python
for i in range(len(tasks)):
    if i == 0:
        total = 1
    else:
        total += tasks[i-1]

    stop_threads = False
    t = threading.Thread(target=runprogress, args=(total, i, lambda: stop_threads))
    t.start()
    time.sleep(random.randint(1, 5)*(self.eta/10))
    stop_threads = True
    t.join()
```

What this does is it creates a loop that will go through every fake task (sleeping). It will start the progress bar, and reset it to the task finished percent when the task is done. After 1 or 2 tasks the progress bar does the math to find the overall average, and sets a good pace. In addition, if the progress bar ever gets to 100% before the tasks are finished, it resets to an average of 83%

### 2.2.2 concurrent.futures

This is used only in 1 area as well to simply get a return value from a function, where the threading module has no easy way to do that. This is just to run a 'loading tasks' popup while the tasks are being generated. Most of the delay is artifical.

```python
stop_threads = False
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(loadtasks)

    if self.eta > 5:
        future2 = executor.submit(start, lambda: stop_threads)

    tasks = future.result()
    stop_threads = True
```

This uses the same technique to have the function stop itself. Next we will look at the function that actaully makes the random tasks.

## 2.3 Generating Tasks

This will show code examples on how the tasks were generated and why they were generated that way.

> Note: This is all part of the [SimulateTasks()](./README.md#17-loadingbarsimulatetasks) example class to show whats possible with this module, and to prove that this module can be used in real world application.

Heres a list in order of what the the method loadtasks() is doing.

1. Chooses how many tasks there should be, anywhere between 2 and 5
1. Creates those tasks that take up a random percent of the total, anywhere bewteen 20 and 60 percent
1. Loops through and slowly ticks down each task after all are created to make sure they sum up to 100
1. Appends each percent that each task takes to a list, and returns that list.

This is why the code example above has:

```python
future = executor.submit(loadtasks)
tasks = future.result()
```

Now lets go over each step and how its implemented.

- Choose how many tasks there should be

```python
ntasks = random.randint(2, 5)
```

- Creates those tasks that take up a random percent of the total

```python
totalperc = self.total

for i in range(ntasks):
    if ntasks == 1:
        j = 100
    else:
        j = random.randint(2, 6) * 10
        j *= (random.randint(95, 105) / 100)

    totalperc -= j
```

- Loops through and slowly ticks down each tasks after all are created to make sure they sum up to 100

This part also rounds each percent to an integer, because the progress bar doesn't support floats (yet).

```python
while totalperc < 0:
    j -= 1
    totalperc += 1
    for ii in range(len(tasks)):
        if tasks[ii] < 5:
            continue
        else:
            tasks[ii] = tasks[ii] - 1
            totalperc += 1

if i == ntasks-1:
    if totalperc != 0:
        tasks[-1] += totalperc

j = round(j, 1)
tasks.append(j)
```

- Appends each percent that each task takes to a list, and returns that list

This part in the code also has some artifical delay to make the 'loading tasks' indicator show up for more than 0.001 seconds. This is not required so its not shown in this example.

```python
tasks = []

for i in range(len(tasks)):
    tasks[i] = round(tasks[i], 1)

return tasks
```

## 2.4 Other

The only other thing in the [SimulateTasks()](./README.md#17-loadingbarsimulatetasks) class that wasn't included was the print statements. It starts by using the [start()](#start) method. The reason this is a method is because the '/' character next to the 'Loading Tasks' rotates in a circle. The code for this can be seen [here](#start).

```txt
Loading Tasks /
```

```txt
Running Tasks...
        |███████████████     |  79%  [eta=00:07.07] [tasks=4/5]
```

The end just calls the [end()](#end) method, which as explained in the main documentation, is just a progress bar with all values maxed out.

```txt
Finshed
        |████████████████████| 100%  [tasks=5/5]
```

## 2.5 start()

This start method is very simple, and is coded like this:

```python
def start(self, stop=False, title='Loading Tasks'):
    percsyms = ['|', '/', '-', '\\']

    j = 0
    while True:
        if stop():
            break

        print('%s %s' % (title, percsyms[j]), end='\r')

        j += 1
        if j == 4:
            j = 1

        time.sleep(0.2)

    print(self.title)
```

Notice that this requires to be stopped by an outside peice of code, so this is not a one-off method that you can just run, un-like [end()](#end).

## 2.6 end()

This method is simply called like this:

```python
lb.end()
```

The code for this method is here:

```python
def end(self, tasks=None, title='Finished'):
        bar  = self.barChar * self.barLength

        if tasks == None:
            total_tasks = self.totalTasks
        else:
            total_tasks = tasks

        print(f"\033[F{title}\t\t\t\t\t\t\t\t\t") # tabs are here just for security

        if total_tasks == None:
            print(f'\t{self.bracketChars[0]}
            {bar}{self.bracketChars[1]} 100{self.percChar}')
        else:
            print(f'\t{self.bracketChars[0]}{bar}{self.bracketChars[1]}
            100{self.percChar}  [tasks={total_tasks}/{total_tasks}]')
```

> Note: All code examples here don't have comments to save space. If you want to view the full code, click [here](https://github.com/flamechain/Modules/blob/main/loadingbar.py).

## 2.7 Conclusion

More sections will be made once new methods or classes get added. You can view future updates on the Main Documentation file on my github.

___

<sub>Documentation Version 1.14 - Module Version 1.1.7 - Release 1.2 - Status = Public</sub>
