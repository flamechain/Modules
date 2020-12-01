# LoadingBar Documentation

Version: 1.1.6

Description: A module to make easy progress bars with built-in examples

___

## Contents

| Title |
|-|
| [Advanced Features](#Advanced-Features) |
| [All Features](#All-Features) |
| [Bar() Class](#loadingbar.Bar()) |
| [Conclusion](#Conclusion) |
| [Future Features](#Future-Features) |
| [Future Updates](#Future-Updates) |
| [Known Issues](#Known-Issues) |
| [New Changes](#New-Changes) |
| [SimulateTasks() Class](#loadingbar.SimulateTasks()) |
| [Using this Module](#Using) |
| [Version Log](#Version-Log) |
||
| [More Documentation](https://github.com/flamechain/Modules.git)|

___

## New Changes

### Features

- Built in randomized example

### Bugs

- Fixed various bugs

## All Features

- Customiable progress bar
- Used in real application with ability to thread
- If threaded estimated completition and eta check

## Future Features

- Built-in param for making titles
- Positioning ability

> Notice: Please report any bugs directly to me and they will be acknowledged and added to this page.

___

## Installation

You can use this module by downloading the python file [here](https://github.com/flamechain/Modules.git).

Move the file into your python directory by going to AppData\Local\Programs\Python\

```txt
%appdata%\..\Local\Programs\Python\
```

Then locate the current python version, is this case, 3.9.

```txt
\Python39\Lib
```

This folder contains all built-in modules, so just paste the [loadingbar.py](https://github.com/flamechain/Modules.git) file into there.

> Full Path: .\\%appdata%\\..\Local\Programs\Python\Python39\Lib\

___

## loadingbar.Bar()

### Parameters

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| total | Where you put the total percent or other unit that the loading bar reaches at the end. | True | 100
| barLength | The length, in characters, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20
| eta | Used with the [SimulateTasks()](#loadingbar.SimulateTasks()) class, and changes overall delay on the visual. Not exact, only average. Based on seconds. | True | 10
| totalTasks | The total amount of tasks used. If not specified there will be not tasks indicator with the bar. | True | None
| barChar | Used for the moving bar. Often '#' is used. | True | '█'
| arrow | Used for the front character of the bar. Often '>' is used. | True | '█'
| percChar | Used for showing what unit the total is shown in. | True | '%'
| bracketChars | List with 2 indices, the front and last character of the bar. Often '[' and ']' is used. | True | ['&#124;', '&#124;']

### Description

This class takes advantage of the python '\r' or 'replace' ending to make a moving progress bar. Its called simply:

```python
import loadingbar

lb = loadingbar.Bar(args)
```

### total

Changes the number directly after the progress bar itself. In this example its set to the default 100:

```txt
|████████████████████| 100%
```

### barLength

The length if the moving status bar indicator. In this example its set to 20 using the block character:

```txt
|████████████████████|
```

### eta

This is not the eta that shows up on the bar during runtime, but rather an estimated time it will take to complete the bar. Only valid if its for demo purposes and no tasks running.

Rather for future there might be a eta param to toggle the eta status next to the bar. Here is 2 examples of the bar, using the same code:

```txt
|                    |   0%  [eta=00:00.00]
```

```txt
|████████████████████| 100%
```

In the top example the tasks haven't started so an eta can't be calculated. In the bottom example its complete, so the eta box doesn't show up on the screen.

### totalTasks

This is used just for the indicator on the bar to show how many tasks there are. There is no checking if the number of tasks is equal to this value. Both examples use a value of 5:

```txt
|                    |   0%  [tasks=0/5]
```

```txt
|████████████████████| 100%  [tasks=5/5]
```

The top example is before the tasks have started, and the bottom example is after its done. Unlike the eta box, it stays after the tasks are finished.

### barChar

This is simply the character used for the bar:

```txt
|████████████████████| 100%
```

```txt
|####################| 100%
```

The top example uses the default block character, and the bottom one used a pound.

### arrow

This is the head of the current bar status:

```txt
|██████████          |  50%
```

```txt
|#########>          |  50%
```

The top example is the default, and the bottom uses the greater than symbol. The bottom also uses the pound as the barChar because it looks better, and would most likely be used with that more often.

### percChar

This is the unit symbol:

```txt
|████████████████████| 100%
```

This uses the default percent symbol, but others can be used. This would most likey make sense if the total parameter is set to some other value.

### bracketChars

This is a list with the bounds of the bar. The default is the pipe, but with any other character for the bar, e.g. '#', square brackets are more commonly used:

```txt
[####################] 100%
```

___

## Using

### progress()

For this you can call the class like mentioned above, and then use the progress method to change the status of the bar. This is an example using only default values, and setting the status of the bar to 100%.

```python
import loadingbar

lb = loadingbar.Bar()
lb.progress(100)
```

```txt
|████████████████████| 100%
```

You can also add tasks to the bar by adding thath parameter to the [Bar()](#loadingbar.Bar()), and then telling the progress method how many tasks are done.

```python
lb = loadingbar.Bar(totalTasks=10)

for i in range(11):
    percent = i * 10
    lb.progress(percent, tasksDone=i)
```

In this example, every iteration the bar's completion goes up by 10%, and 1 task finishes. Here is the result of the bar after completion.

```txt
|████████████████████| 100%  [tasks=10/10]
```

To use the eta, just specify how long its been since starting. The eta gets automatically calculated from there.

```python
import loadingbar, time

lb = loadingbar.Bar(totalTasks=10)
startTime = time.time()

for i in range(11):
    percent = i * 10
    currentTime = time.time() - startTime

    lb.progress(percent, time_=currentTime, tasksDone=i)

    time.sleep(0.1)
```

In this example, we use the time module to calculate how many seconds have passed. Then we simple pass how much time has elapsed into the bar. This is what the bar would look like at iteration 6, just over half way. Notice how we also used time.sleep() to make it look more real.

```txt
|████████████        |  60%  [eta=00:04.36] [tasks=6/10]
```

### start()

This method is not used often, because most people would rather not have a flashy intro, or it doesn't fit there requirments.

```txt
Loading Tasks /
```

It simple runs a spinning bar until stopped. You can stop this method by triggering the stop parameter, which stops itself.

```python
import loadingbar, time, concurrent.futures

lb = loadingbar.Bar()

stop_threads = False
with concurrent.futures.ThreadPoolExecutor() as executor:
    future2 = executor.submit(lb.start, lambda: stop_threads)

    time.sleep(1)

    stop_threads = True
```

This example uses the concurrent module to thread this task, so the thread can be manipulated while running. When run this program will run the 'loading tasks' prompt for 1 second, then the program will stop. This print() statement uses '\r' or 'replace' so you can take advantage by completely clearing it from the screen after finished.

### end()

This is used much more often. What this does is it just prints the loadingbar with all values maxed out, and eta gone (if there was one).

```python
lb = loadingbar.Bar(totalTasks=5)

lb.end()
```

```txt
|████████████████████| 100%  [tasks=5/5]
```

___

## loadingbar.SimulateTasks()

### Parameters (SimulateTasks)

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| eta | Changes overall delay on the visual. Not exact, only average. Based on seconds | True | 15
| total | .Where you put the total percent or other unit that the loading bar reaches at the end. | True | 100
| barLength | The length, in characters, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20

All parameters have been explained above in the [Bar()](#loadingbar.Bar()) parameters section. These values go directly into that class.

### Example

This has been shown above, but here are a couple examples of the output it could print.

Start

```txt
Loading Tasks /
```

Middle

```txt
Running Tasks...
        |███████████████     |  79%  [eta=00:07.07] [tasks=4/5]
```

End

```txt
Finshed
        |████████████████████| 100%  [tasks=5/5]
```

## Conclusion

This is the end of the basics for this module. All the more technical stuff goes after this point.

___

## Advanced Features

### pastBar

This is a parameter to the progress method. All of progress's methods will we listed here.

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| current | Current percentage you want the bar to show. | False |
| time_ | How long has elapsed since the start of the bar. Used for eta. | True | None |
| tasksDone | How many tasks are complete. Used for visualization | True | 0 |
| pastBar | Used for dynamic animation. | True | None |

pastBar is at the bottom because its hardest to use. Basically progress will return a value if this is not None, and then you put that value back into progress.

```python
past = 0
past = lb.progress(0, pastBar=past)

time.sleep(1)
past = lb.progress(50, pastBar=past)

time.sleep(1)
past = lb.progress(100, pastBar=past)
```

Each second it will jump up by 50 percent, but the bar will update each character with a tiny delay, so it appears to go up more slowly, instead of a sudden jump.

> Note: The __progress()__ method only returns when __pastBar__ is specified, thats why the past variable needed to be defined first so it could be used for the first iteration. Likewise at the end, the past var is not doing anything, just a placeholder for the return value.

___

## Version Log

| Version | New Changes | Release Date |
|-|-|:-:|
| 1.1.6 | Added [bug log](#Bug-log) and fixed [bugs](#Bug-Log) | 12/01/20 |
| 1.1.5 | Various bug fixes, added [version log](#Version-Log) | 12/01/20 |
| 1.1.4 | Various bug fixes | 12/01/20 |
| 1.1.3 | Various bug fixes, added [documentation](#LoadingBar-Documentation) | 11/30/20 |
| 1.1.2 | Various bug fixes | 11/30/20 |
| 1.1.1 | Various bug fixes | 11/30/20 |
| 1.1.0 | Added [SimulateTasks()](#loadingbar.SimulateTasks()) class to main module | 11/29/20 |
| 1.0.2 | Various bug fixes | 11/29/20 |
| 1.0.1 | Converted [SimulateTasks()](#loadingbar.SimulateTasks()) to class form | 11/28/20 |
| 1.0.0 | Inital Release | 11/27/20 |

Pre-Release Version

| Stage | Version ID | New Changes | Release Date |
|:-:|-|-|:-:|
| beta | 3.0 | Threading with eta estimation | 11/27/20 |
| beta | 2.0 | Tasks visual and ability to detect them | 11/26/20
| beta | 1.3 | Various big fixes | 11/26/20
| beta | 1.2 | Loading bar now has eta display | 11/26/20 |
| beta | 1.1 | Loading bar with percent of completion | 11/25/20 |
| beta | 1.0 | Dynamic loading bar | 11/25/20 |
| alpha | 1.2 | Eta calculator | 11/25/20 |
| alpha | 1.1 | Class form | 11/25/20 |
| alpha | 1.0 | First version, only progress method as single function | 11/24/20 |

___

## Known Issues

> Note: This bug log only contains bugs going back to version 1.1.6

| Version | Bug ID | Description | Status | Fix Date |
|-|-|-|:-:|:-:|
| 1.1.6 | 001 | time_ param in progress() method froze program if over 100 | Fixed | 12/01/20 |

___

## Future Big Updates

> Note: These release dates aren't offical and are only estimations

| Version | Planned Changes | Release Date |
|-|-|:-:|
| 1.5.0 | Extensions including pre-sets and color | 01/20/20 |
| 1.4.0 | More features including multi-bar version, and different types of progress indicators. | 01/10/21 |
| 1.3.0 | Compatibility with non-terminal formats. | 12/20/20 |
| 1.2.0 | Ability to change bar format, pre-sets, and more than 1 example class. | 12/10/20 |

<sub>Documentation Version 1.0 - Module Version 1.1.6 - Release 1.0 - Status = Public</sub>
