# Version 1.1.9
import time, random, concurrent.futures, threading, termcolor

class Bar:
    def __init__(self, total=100, barLength=20, eta=0, totalTasks=None, barChar='█', arrow='█', percChar='%', bracketChars=['|', '|'], title='Running Tasks...', color=False):
        '''
        ### Description

        Loading/Progress bar for general use. Use SimulateTasks() to see this used in a way possible.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | total | True | Total percentage. |
        | barLength | True | Length of bar in characters. |
        | eta | True | Way to change the average time taken, in seconds. |
        | totalTasks | True | Amount of tasks to get done, just for visualization. |
        | barChar | True | The character that the bar is made of. Default = █, but # is also common. |
        | arrow | True | Head of the bar, usally same as barChar or >. |
        | percChar | True | Symbol for percent, made so total can be some other unit. |
        | bracketChars | True | List with start bar and end bar bracket. [] is common, || is default. |
        | title | True | Title that shows up for the progress bar. Actaully gets prinited using the start() method. |

        Github Link: https://github.com/flamechain/Modules
        '''
        self.barLength = barLength
        self.total = total
        self.eta = eta / 10
        self.totalTasks = totalTasks
        self.barChar = barChar
        self.arrow = arrow
        self.percChar = percChar
        self.bracketChars = bracketChars
        self.title = title
        
        if color:
            self.green = 'green'
        else:
            self.green = 'white'

    def start(self, stop=False, title='Loading Tasks'):
        '''
        ### Description

        Made for threading while initilizing tasks. Not Required to use.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | stop | True | Call this to stop itself. |
        | title | True | The title that is used while this is running. |

        Github Link: https://github.com/flamechain/Modules
        '''
        percsyms = ['|', '/', '-', '\\']

        j = 0
        while True: # Runs until stopped by stop()
            if stop():
                break

            print('%s %s' % (title, percsyms[j]), end='\r')

            j += 1
            if j == 4:
                j = 1

            time.sleep(0.2)
        
        print(self.title)

    def progress(self, current, time_=None, tasksDone=0, pastBar=None):
        '''
        ### Description

        The loading bar itself. Doesn't iterate itself.

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | current | False | Current percentage that the bar has completed. |
        | time_ | True | How long its taken so far. Used for calculating eta. |
        | tasksDone | True | Amount of tasks done, just for visualization. |
        | pastBar | True | Used if you don't have threading, but want a nice animation to get to current percent. |

        Github Link: https://github.com/flamechain/Modules
        '''
        # Generates Bar Format
        percent = float(current) * 100 / self.total
        bar = self.barChar * int(percent/100 * self.barLength - 1) + self.arrow
        spaces  = ' ' * (self.barLength - len(bar))
        space = ' ' * (5 - len(str(percent)))

        # Creates an eta (if possible)
        try:
            eta = str(round((time_ * (100/current)) - time_, 2))
            eta, et2 = eta.split('.')
            et3 = '00'

            while int(eta) > 59:
                eta = str(int(eta) - 60)
                et3 = str(int(et3) + 1)

            if len(et2) == 1:
                et2 = et2 + '0'
            if len(eta) == 1:
                eta = '0' + eta

            eta = ':'.join([str(et3), str(eta)])
            eta = '.'.join([str(eta), str(et2)])

        except:
            eta = '00:00.00'

        # pastBar fork
        if pastBar != None:
            temp1 = 1
            temp2 = pastBar
            while len(bar) > pastBar:
                string_ = '\t%s%s%s%s%s %s%d%s  [eta=%s] [tasks=%s/%s]' % (self.bracketChars[0], self.barChar * temp2, termcolor.colored(self.barChar * temp1, self.green),
                (spaces + (" " * (len(bar)-pastBar-1))), self.bracketChars[1], space, percent, self.percChar, eta, tasksDone, self.totalTasks)
                print(string_, end='\r')
                pastBar += 1
                temp1 += 1
                time.sleep(0.05)

            string_ = string_.replace(self.barChar, termcolor.colored(self.barChar, 'white'))
            print(string_, end='\r')
            return len(bar)

        # Prints all values it has
        else:
            if (time_ == None) & (self.totalTasks == None):
                print('\t%s%s%s%s %s%d%s' % (self.bracketChars[0], bar, spaces, self.bracketChars[1], space, percent, self.percChar), end='\r')
            elif (time_ == None) & (self.totalTasks != None):
                print('\t%s%s%s%s %s%d%s  [tasks=%s/%s]' % (self.bracketChars[0], bar, spaces, self.bracketChars[1], space, percent, self.percChar, tasksDone, self.totalTasks), end='\r')
            elif (time != None) & (self.totalTasks == None):
                print('\t%s%s%s%s %s%d%s  [eta=%s]' % (self.bracketChars[0], bar, spaces, self.bracketChars[1], space, percent, self.percChar, eta), end='\r')
            elif (time != None) & (self.totalTasks != None):
                print('\t%s%s%s%s %s%d%s  [eta=%s] [tasks=%s/%s]' % (self.bracketChars[0], bar, spaces, self.bracketChars[1], space, percent, self.percChar, eta, tasksDone, self.totalTasks), end='\r')
            eta_, eta2_ = eta.split(':')

            while int(eta_) != 0:
                eta_ = int(eta_) - 1
                eta2_ = float(eta2_) + 60

            if (eta2_ == 0) | (self.total-current == 0):
                time.sleep(0.01)
            else:
                time.sleep((float(eta2_)/(self.total-current)))

    def end(self, tasks=None, title='Finished'):
        '''
        ### Description

        Shows full bar complete, and removes eta and shows all tasks complete (if any).

        ### Params

        | Name | Optional | Description |
        |-|:-:|-|
        | tasks | True | Optional param if you want to use external tasks. |
        | title | True | Title that prints when the progress bar is done. |

        Github Link: https://github.com/flamechain/Modules
        '''
        bar  = self.barChar * self.barLength

        if tasks == None:
            total_tasks = self.totalTasks
        else:
            total_tasks = tasks

        print("\033[F" + termcolor.colored(title, self.green) + "\t\t\t\t\t\t\t\t")

        # Puts in all values at max
        if total_tasks == None:
            print(f'\t{self.bracketChars[0]}{bar}{self.bracketChars[1]}', end='')
            print(termcolor.colored(' 100' + self.percChar, self.green))
        else:
            print(f'\t{self.bracketChars[0]}{bar}{self.bracketChars[1]}', end='')
            print(termcolor.colored(' 100' + self.percChar + f'  [tasks={total_tasks}/{total_tasks}]', self.green))

class SimulateTasks:
    def __init__(self, eta=15, total=100, barLength=20, *args):
        '''
        ### Description

        Custom use of Bar() class

        ### Params
        
        | Name | Optional | Description |
        |-|:-:|-|
        | eta | True | Bar() eta param, used for average time. |
        | total | True | Total percentage of the bar. |
        | barLength | True | Length of the bar in characters. |
        ||||
        | *args | True | If you want to use external task values for unit testing. |

        Github Link: https://github.com/flamechain/Modules
        '''
        self.barLength = barLength
        self.eta = eta
        self.total = total
        self.simulateTasks
        self.tasks = args
        self.simulateTasks()

    def simulateTasks(self):
        # Checks if pre-loaded tasks (*args) and then generates tasks if not
        if len(self.tasks) > 0:
            tasks = self.tasks
            total_ = 0
            for i in tasks:
                total_ += i
            if self.total < total_:
                return print('Value Error: Your custom tasks exceded the total (%s > %s)' % (total_, self.total))
            elif self.total > total_:
                print(termcolor.colored(f'Warning: Your custom tasks did not reach the total ({total_} < {self.total})', 'red'))
                print(termcolor.colored('The Program will continue but there may be errors.', 'red'), end='\n\n')
                time.sleep(2)
                stop_threads = False
                lb = Bar(self.total, self.barLength, self.eta)
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(lb.start, lambda: stop_threads)
                    time.sleep(1)
                    stop_threads = True
        else:
            stop_threads = False
            lb = Bar(self.total, self.barLength, self.eta)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.loadtasks)
                if self.eta > 5:
                    future2 = executor.submit(lb.start, lambda: stop_threads)
                tasks = future.result()
                stop_threads = True

        start_time = time.time()
        lb = Bar(self.total, self.barLength, self.eta, len(tasks))
        current = 0

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

        # Creates inital speed for progress bar
        totaltime = time.time() - start_time
        total = 0
        lb.progress(total, totaltime)
        time.sleep(0.005*self.eta)
        totaltime = time.time() - start_time
        lb.progress(total+1, totaltime)

        # Runs each task
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

        # Ends
        time.sleep(0.1)
        lb.end((len(tasks)))

    def loadtasks(self):
        # Picks how many tasks to make
        ntasks = random.randint(2, 5)
        tasks = []
        totalperc = self.total

        for i in range(ntasks):
            # Creates tasks
            if ntasks == 1:
                j = 100
            else:
                j = random.randint(2, 6) * 10
                j *= (random.randint(95, 105) / 100)

            # Tweaks tasks so they sum to total
            totalperc -= j
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

            if self.eta > 5:
                time.sleep((random.randint(25, 75)/100)*(self.eta/10))

        # Returns tasks in a list
        for i in range(len(tasks)):
            tasks[i] = round(tasks[i], 1)

        return tasks
