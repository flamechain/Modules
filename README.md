# 1 LoadingBar Documentation

### Creator: FlameChain

Github Link: [flamechain/Modules/](https://github.com/flamechain/Modules)

### Version: 1.1.7

Description: A module to make easy progress bars with lots of customizability and a built-in demo class to show whats possible.

___

## 1.1 Contents

- [1 LoadingBar Documentation](#1-loadingbar-documentation)
- [1.1 Contents](#11-contents)
- [1.2 New Changes](#12-new-changes)
- [1.3 Future Features](#13-future-features)
- [1.4 Installation](#14-installation)
- [1.5 loadingbar.Bar()](#15-loadingbarbar)
  - [1.5.1 Parameters](#151-parameters)
  - [1.5.2 Description](#152-description)
  - [1.5.3 total](#153-total)
  - [1.5.4 barLength](#154-barlength)
  - [1.5.5 eta](#155-eta)
  - [1.5.6 totalTasks](#156-totaltasks)
  - [1.5.7 barChar](#157-barchar)
  - [1.5.8 arrow](#158-arrow)
  - [1.5.9 percChar](#159-percchar)
  - [1.5.10 bracketChars](#1510-bracketchars)
  - [1.5.11 title](#1511-title)
- [1.6 Using](#16-using)
  - [1.6.1 progress()](#161-progress)
  - [1.6.2 start()](#162-start)
  - [1.6.3 end()](#163-end)
- [1.7 loadingbar.SimulateTasks()](#17-loadingbarsimulatetasks)
  - [1.7.1 Parameters (SimulateTasks)](#171-parameters-simulatetasks)
  - [1.7.2 Example](#172-example)
- [1.8 Conclusion](#18-conclusion)
- [1.9 Advanced Features](#19-advanced-features)
  - [1.9.1 pastBar](#191-pastbar)
- [1.10 Version Log](#110-version-log)
- [1.11 Known Issues](#111-known-issues)
- [1.12 Future Big Updates](#112-future-big-updates)
- [2.0 Secondary Documentation](./MoreDocumentation.md)

___

## 1.2 New Changes

- [Built in randomized example](#18-loadingbarsimulatetasks)
- [Bug fixes](#113-known-issues)
- [title param to make titles](#1611-title)

## 1.3 Future Features

- Positioning ability

> Notice: Please report any bugs directly to me and they will be acknowledged and added to this page.

___

## 1.4 Installation

You can use this module by downloading the python file [here](https://github.com/flamechain/Modules.git).

Move the file into your python directory by going to AppData\Local\Programs\Python\

```txt
%appdata%\..\Local\Programs\Python\
```

Then locate the current python version, is this case, 3.9.

```txt
\Python39\Lib
```

This folder contains all built-in modules, so just paste the [loadingbar.py](https://github.com/flamechain/Modules/blob/main/loadingbar.py) file into there.

> Full Path: .\\%appdata%\\..\Local\Programs\Python\Python39\Lib\

___

## 1.5 loadingbar.Bar()

### 1.5.1 Parameters

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| total | Where you put the __total percent__ or other unit that the loading bar reaches at the end. | True | 100
| barLength | The __length, in characters__, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20
| eta | Used with the [SimulateTasks()](#loadingbar.SimulateTasks()) class, and changes overall delay on the visual. Not exact, only average. Based on seconds. | True | 10
| totalTasks | The __total amount of tasks__ used. If not specified there will be not tasks indicator with the bar. | True | None
| barChar | Used for the moving bar. Often '#' is used. | True | '█'
| arrow | Used for the front character of the bar. Often '>' is used. | True | '█'
| percChar | Used for showing what unit the total is shown in. | True | '%'
| bracketChars | List with 2 indices, the front and last character of the bar. Often '[' and ']' is used. | True | ['&#124;', '&#124;']
| title | What the title is for the progress bar while running. | True | 'Running Tasks...' |

### 1.5.2 Description

This class takes advantage of the python '\r' or 'replace' ending to make a moving progress bar. Its called simply:

```python
import loadingbar

lb = loadingbar.Bar(args)
```

### 1.5.3 total

Changes the number directly after the progress bar itself. In this example its set to the default 100:

```txt
|████████████████████| 100%
```

### 1.5.4 barLength

The length if the moving status bar indicator. In this example its set to 20 using the block character:

```txt
|████████████████████|
```

### 1.5.5 eta

This is not the eta that shows up on the bar during runtime, but rather an estimated time it will take to complete the bar. Only valid if its for demo purposes and no tasks running.

Rather for future there might be a eta param to toggle the eta status next to the bar. Here is 2 examples of the bar, using the same code:

```txt
|                    |   0%  [eta=00:00.00]
```

```txt
|████████████████████| 100%
```

In the top example the tasks haven't started so an eta can't be calculated. In the bottom example its complete, so the eta box doesn't show up on the screen.

### 1.5.6 totalTasks

This is used just for the indicator on the bar to show how many tasks there are. There is no checking if the number of tasks is equal to this value. Both examples use a value of 5:

```txt
|                    |   0%  [tasks=0/5]
```

```txt
|████████████████████| 100%  [tasks=5/5]
```

The top example is before the tasks have started, and the bottom example is after its done. Unlike the eta box, it stays after the tasks are finished.

### 1.5.7 barChar

This is simply the character used for the bar:

```txt
|████████████████████| 100%
```

```txt
|####################| 100%
```

The top example uses the default block character, and the bottom one used a pound.

### 1.5.8 arrow

This is the head of the current bar status:

```txt
|██████████          |  50%
```

```txt
|#########>          |  50%
```

The top example is the default, and the bottom uses the greater than symbol. The bottom also uses the pound as the barChar because it looks better, and would most likely be used with that more often.

### 1.5.9 percChar

This is the unit symbol:

```txt
|████████████████████| 100%
```

This uses the default percent symbol, but others can be used. This would most likey make sense if the total parameter is set to some other value.

### 1.5.10 bracketChars

This is a list with the bounds of the bar. The default is the pipe, but with any other character for the bar, e.g. '#', square brackets are more commonly used:

```txt
[####################] 100%
```

## 1.5.11 title

Title for the progress bar while running. The default is 'Running Tasks...', but it could be anything.

```txt
Running Tasks...
        |██████████          |  50%
```

___

## 1.6 Using

### 1.6.1 progress()

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
Finished
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

### 1.6.2 start()

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

### 1.6.3 end()

This is used much more often. What this does is it just prints the loadingbar with all values maxed out, and eta gone (if there was one).

```python
lb = loadingbar.Bar(totalTasks=5)

lb.end()
```

```txt
Finished
        |████████████████████| 100%  [tasks=5/5]
```

___

## 1.7 loadingbar.SimulateTasks()

### 1.7.1 Parameters (SimulateTasks)

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| eta | Changes overall delay on the visual. Not exact, only average. Based on seconds | True | 15
| total | .Where you put the total percent or other unit that the loading bar reaches at the end. | True | 100
| barLength | The length, in characters, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20

All parameters have been explained above in the [Bar()](#loadingbar.Bar()) parameters section. These values go directly into that class.

### 1.7.2 Example

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

## 1.8 Conclusion

This is the end of the basics for this module. All the more technical stuff goes after this point.

___

## 1.9 Advanced Features

### 1.9.1 pastBar

This is a parameter to the progress method. All of progress's methods will we listed here.

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| current | __Current percentage__ you want the bar to show. | False |
| time_ | How long has __elapsed since the start__ of the bar. Used for eta. | True | None |
| tasksDone | How many __tasks are complete__. Used for visualization | True | 0 |
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

> Note: The [__progress()__](#161-progress) method only returns when __pastBar__ is specified, thats why the past variable needed to be defined first so it could be used for the first iteration. Likewise at the end, the past var is not doing anything, just a placeholder for the return value.

___

## 1.10 Version Log

| Version | New Changes | Release Date |
|-|-|:-:|
| 1.1.7 | [SimulateTasks()](#loadingbar.SimulateTasks()) no longer has nested functions, and doesn't have its own redundent [start()](#162-start()) method. Also added title param to all methods so printing the title is built in. | 12/01/20 |
| 1.1.6 | Added [bug log](#Bug-log) and fixed [bugs](#Bug-Log) | 12/01/20 |
| 1.1.5 | Bug fixes, added [version log](#Version-Log) | 12/01/20 |
| 1.1.4 | Bug fixes | 12/01/20 |
| 1.1.3 | Bug fixes, added [documentation](#LoadingBar-Documentation) | 11/30/20 |
| 1.1.2 | Bug fixes | 11/30/20 |
| 1.1.1 | Bug fixes | 11/30/20 |
| 1.1.0 | Added [SimulateTasks()](#loadingbar.SimulateTasks()) class to main module | 11/29/20 |
| 1.0.2 | Bug fixes | 11/29/20 |
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

## 1.11 Known Issues

> Note: This bug log only contains bugs going back to version 1.1.6

| Version | Bug ID | Description | Status | Fix Date |
|-|-|-|:-:|:-:|
| 1.1.6 | 001 | time_ param in progress() method froze program if over 100 | Fixed | 12/01/20 |

___

## 1.12 Future Big Updates

> Note: These release dates aren't offical and are only estimations

| Version | Planned Changes | Release Date |
|-|-|:-:|
| 1.5.0 | Extensions including pre-sets and color | 01/20/20 |
| 1.4.0 | More features including multi-bar version, and different types of progress indicators. | 01/10/21 |
| 1.3.0 | Compatibility with non-terminal formats. | 12/20/20 |
| 1.2.0 | Ability to change bar format, pre-sets, and more than 1 example class. | 12/10/20 |

<sub>Documentation Version 1.14 - Module Version 1.1.7 - Release 1.2 - Status = Public</sub>
