# LoadingBar Documentation (Part 2)

# NOTE: WORK IN PROGRESS

Version: 1.1.6

Description: Extra documentation with larger and more specific examples.

___

## Contents

| Title |
|-|
| [Threading](#Threading) |
||
| [Main Documentation](https://github.com/flamechain/Modules.git) |

___

## Threading

This section will mainly just go over how the SimulateTasks() class worked. You can always look at the code yourself [here](https://github.com/flamechain/Modules.git).

> Note: The SimulateTasks() class is an example class without strict formatting, so it may be more difficult to read.

### threading.Thread

In the SimulateTasks() class it uses the threading and concurrent modules. This section will go over just where it used the threading module to make it apear like its estimating eta without know how long the tasks will take.

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

### concurrent.futures

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

## Random Tasks

This will show code examples on how the tasks were generated and why they were generated that way.
