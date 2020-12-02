# 1 LoadingBar Documentation

## Creator: FlameChain

Github Link: [flamechain/Modules/](https://github.com/flamechain/Modules)

### Version: 1.2.0

Description: A module to make easy progress bars with lots of customizability and a built-in demo class to show whats possible.

___

## 1.1 Contents

- [1 LoadingBar Documentation](#1-loadingbar-documentation)
- [1.1 Contents](#11-contents)
- [1.2 New Changes](#12-new-changes)
- [1.3 Installation](#13-installation)
- [1.4 loadingbar.Bar()](#14-loadingbarbar)
  - [1.4.1 Parameters](#141-parameters)
  - [1.4.2 Description](#142-description)
  - [1.4.3 BarLength](#143-barlength)
  - [1.4.4 EstimatedTotalTime](#144-estimatedtotaltime)
  - [1.4.5 TaskCount](#145-taskcount)
  - [1.4.6 MainBarChar](#146-mainbarchar)
  - [1.4.7 ProgressPointBarChar](#147-progresspointbarchar)
  - [1.4.8 EndPointChars](#148-endpointchars)
  - [1.4.9 Title](#149-title)
  - [1.4.10 UseColor](#1410-useColor)
- [1.5 Using](#15-using)
  - [1.5.1 Progress()](#151-progress)
  - [1.5.2 Start()](#152-start)
  - [1.5.3 End()](#153-end)
- [1.6 Loadingbar.SimulateTasks()](#16-loadingbarsimulatetasks)
  - [1.6.1 Parameters (SimulateTasks)](#161-parameters-simulatetasks)
  - [1.6.2 Example](#162-example)
- [1.7 Conclusion](#17-conclusion)
- [1.8 Advanced Features](#18-advanced-features)
  - [1.8.1 PastBar](#181-pastbar)
  - [1.8.2 *args](#182-simulatetasks-args)
- [1.9 Version Log](#19-version-log)
- [1.10 Known Issues](#110-known-issues)
- [1.11 Future Big Updates](#111-future-big-updates)
- [2.0 Secondary Documentation](./MoreDocumentation.md)

___

## 1.2 New Changes

- [Renamed all params](#141-parameters)
- [Color](#1410-useColor)
- [Bug fixes](#110-known-issues)

> Notice: Please report any bugs directly to me and they will be acknowledged and added to this page.

___

## 1.3 Installation

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

## 1.4 loadingbar.Bar()

### 1.4.1 Parameters

| Param Name | Description | Type | Default |
|-|-|:-:|-|
| barLength | The __length, in characters__, that the bar progress bar expands. This only includes the moving part of the bar. | integer | 20
| estimatedTotalTime | Used with the [SimulateTasks()](#16-loadingbarsimulatetasks) class, and changes overall delay on the visual. Not exact, only average. Based on seconds. | float | 10
| taskCount | The __total amount of tasks__ used. If not specified there will be not tasks indicator with the bar. | integer | None
| mainBarChar | Used for the moving bar. Often '#' is used. | string | '█'
| progressPointBarChar | Used for the front character of the bar. Often '>' is used. | string | '█'
| endPointChars | List with 2 indices, the front and last character of the bar. Often '[' and ']' is used. | list | ['&#124;', '&#124;']
| title | What the title is for the progress bar while running. | string | 'Running Tasks...' |
| useColor | If you want to have some color in on the bar. | boolean | False |

### 1.4.2 Description

This class takes advantage of the python '\r' or 'replace' ending to make a moving progress bar. Its called simply:

```python
import loadingbar

lb = loadingbar.Bar(args)
```

### 1.4.3 barLength

The length if the moving status bar indicator. In this example its set to 20 using the block character:

```txt
|████████████████████|
```

### 1.4.4 estimatedTotalTime

This is not the eta that shows up on the bar during runtime, but rather an estimated time it will take to complete the bar. Only valid if its for demo purposes and no tasks running.

Rather for future there might be a eta param to toggle the eta status next to the bar. Here is 2 examples of the bar, using the same code:

```txt
|                    |   0%  [eta=00:00.00]
```

```txt
|████████████████████| 100%
```

In the top example the tasks haven't started so an eta can't be calculated. In the bottom example its complete, so the eta box doesn't show up on the screen.

### 1.4.5 taskCount

This is used just for the indicator on the bar to show how many tasks there are. There is no checking if the number of tasks is equal to this value. Both examples use a value of 5:

```txt
|                    |   0%  [tasks=0/5]
```

```txt
|████████████████████| 100%  [tasks=5/5]
```

The top example is before the tasks have started, and the bottom example is after its done. Unlike the eta box, it stays after the tasks are finished.

### 1.4.6 mainBarChar

This is simply the character used for the bar:

```txt
|████████████████████| 100%
```

```txt
|####################| 100%
```

The top example uses the default block character, and the bottom one used a pound.

### 1.4.7 progressPointBarChar

This is the head of the current bar status:

```txt
|██████████          |  50%
```

```txt
|#########>          |  50%
```

The top example is the default, and the bottom uses the greater than symbol. The bottom also uses the pound as the barChar because it looks better, and would most likely be used with that more often.

### 1.4.8 endPointChars

This is a list with the bounds of the bar. The default is the pipe, but with any other character for the bar, e.g. '#', square brackets are more commonly used:

```txt
[####################] 100%
```

## 1.4.9 title

Title for the progress bar while running. The default is 'Running Tasks...', but it could be anything.

```txt
Running Tasks...
        |██████████          |  50%
```

## 1.4.10 useColor

Boolian used if you want to have some color. Currently color param only applies to the base class, not the [SimulateTasks()](#16-loadingbarsimulatetasks) class, hence an error message on [SimulateTasks()](#16-loadingbarsimulatetasks) is always red. Default to off because its purely visual and personal preference. This color appears when the [end()](#153-end) method is called:

<pre>
<span style="color:green">Finished</span>
        |████████████████████| <span style="color:green">100%</span>
</pre>

And also when the pastBar progress bar is being updated, the knew progress is green until its to the right point.

___

## 1.5 Using

### 1.5.1 progress()

For this you can call the class like mentioned above, and then use the progress method to change the status of the bar. This is an example using only default values, and setting the status of the bar to 100%.

```python
import loadingbar

lb = loadingbar.Bar()
lb.progress(100)
```

```txt
|████████████████████| 100%
```

You can also add tasks to the bar by adding thath parameter to the [Bar()](#14-loadingbarbar), and then telling the progress method how many tasks are done.

```python
lb = loadingbar.Bar(taskCount=10)

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

lb = loadingbar.Bar(taskCount=10)
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

### 1.5.2 start()

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

### 1.5.3 end()

This is used much more often. What this does is it just prints the loadingbar with all values maxed out, and eta gone (if there was one).

```python
lb = loadingbar.Bar(taskCount=5)

lb.end()
```

```txt
Finished
        |████████████████████| 100%  [tasks=5/5]
```

___

## 1.6 loadingbar.SimulateTasks()

### 1.6.1 Parameters (SimulateTasks)

| Param Name | Description | Optional | Default |
|-|-|:-:|-|
| eta | Changes overall delay on the visual. Not exact, only average. Based on seconds | True | 15
| total | .Where you put the total percent or other unit that the loading bar reaches at the end. | True | 100
| barLength | The length, in characters, that the bar progress bar expands. This only includes the moving part of the bar. | True | 20

All parameters have been explained above in the [Bar()](#14-loadingbarbar) parameters section. These values go directly into that class.

### 1.6.2 Example

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

## 1.7 Conclusion

This is the end of the basics for this module. All the more technical stuff goes after this point.

___

## 1.8 Advanced Features

### 1.8.1 pastBar

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

> Note: The [__progress()__](#151-progress) method only returns when __pastBar__ is specified, thats why the past variable needed to be defined first so it could be used for the first iteration. Likewise at the end, the past var is not doing anything, just a placeholder for the return value.

### 1.8.2 SimulateTasks() *args

This is a parameter in the [SimulateTasks()](#16-loadingbarsimulatetasks) class that lets you put in custom test-cases. Here is an example of how its used:

> Note: The first 2 values aren't tasks, just there so *args gets properly evaluated.

```python
lb.SimulateTasks(15, 20, 50, 20, 30)
```

In this example there are 3 custom tasks. The first one takes 50%, the next takes 20%, and the last takes the final 30%. If these values are greater than the total, then an error will be raised.

```python
lb.SimulateTasks(15, 20, 50, 50, 10)
```

```txt
Value Error: Your custom tasks exceded the total (150 > 100)
```

If these values are less than, it will prompt a warning for 2 seconds, and then contiue the program as normal.

<pre>
<span style="color:red">Warning: Your custom tasks did not reach the total (50 < 100)
The Program will continue but there may be errors.</span>
</pre>

___

## 1.9 Version Log

| Version | New Changes | Release Date |
|-|-|:-:|
| 1.2.0 | Changed all param names to be more clear, and removed some useless ones. Overall easier to use. | 12/02/20 |
| 1.1.9 | Added colors to [end()](#153-end) method, and [pastBar](#181-pastbar). Added color param to [Bar()](#14-loadingbarbar) class so the user has the ability to toggle color mode. | 12/02/20 |
| 1.1.8 | [SimulateTasks()](#16-loadingbarsimulatetasks) has an *args param to accept custom pre-set tasks. Updated all doc-strings and added technical comments. | 12/01/20 |
| 1.1.7 | [SimulateTasks()](#16-loadingbarsimulatetasks) no longer has nested functions, and doesn't have its own redundent [start()](#152-start) method. Also added title param to all methods so printing the title is built in. | 12/01/20 |
| 1.1.6 | Added [bug log](#110-known-issues) and fixed [bugs](#110-known-issues) | 12/01/20 |
| 1.1.5 | Bug fixes, added [version log](#19-version-Log) | 12/01/20 |
| 1.1.4 | Bug fixes | 12/01/20 |
| 1.1.3 | Bug fixes, added [documentation](#1-loadingbar-documentation) | 11/30/20 |
| 1.1.2 | Bug fixes | 11/30/20 |
| 1.1.1 | Bug fixes | 11/30/20 |
| 1.1.0 | Added [SimulateTasks()](#16-loadingbarsimulatetasks) class to main module | 11/29/20 |
| 1.0.2 | Bug fixes | 11/29/20 |
| 1.0.1 | Converted [SimulateTasks()](#16-loadingbarsimulatetasks) to class form | 11/28/20 |
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

## 1.10 Known Issues

> Note: This bug log only contains bugs going back to version 1.1.6

| Version | Bug ID | Description | Status | Fix Date |
|-|-|-|:-:|:-:|
| 1.1.8 | 002 | pastBar would freeze program | Fixed | 12/02/20 |
| 1.1.6 | 001 | time_ param in progress() method froze program if over 100 | Fixed | 12/01/20 |

___

## 1.11 Future Big Updates

> Note: These release dates aren't offical and are only estimations

| Version | Planned Changes | Release Date |
|-|-|:-:|
| 1.5.0 | Extensions including pre-sets | 01/20/20 |
| 1.4.0 | More features including multi-bar version, and different types of progress indicators. | 01/10/21 |
| 1.3.0 | Compatibility with non-terminal formats. | 12/20/20 |
| 1.2.0 | Ability to change bar format, pre-sets, and more than 1 example class. | 12/10/20 |

<sub>Documentation Version 2.0 - Module Version 1.2.0 - Release 1.5 - Status = Public</sub>
