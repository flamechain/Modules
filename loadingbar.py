# Version 1.1.7
import time, random, concurrent.futures, threading

class Bar:
    '''
    Loading/Progress bar for general use.

    Use SimulateTasks() to see this used in a way possible
    '''
    def __init__(self, total=100, barLength=20, eta=0, totalTasks=None, barChar='█', arrow='█', percChar='%', bracketChars=['|', '|'], title='Running Tasks...'):
        '''
        # Params
        total = total percentage

        barLength = length of bar in characters


        # Optional Params
        eta = way to change the average time taken, in seconds;

        totalTasks = amount of tasks to get done, just for visualization;

        barChar = the character that the bar is made of. Default = █, but # is also common;

        arrow = head of the bar, usally same as barChar or >;

        percChar = symbol for percent, made so total can be some other unit;

        bracketChars = list with start bar and end bar bracket. [] is common, || is default;

        title = Title that shows up for the progress bar. Actaully gets prinited using the start() method;
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

    def start(self, stop=False, title='Loading Tasks'):
        '''
        Made for threading while initilizing tasks. Not Required to use.

        # Optional Params
        stop = call this to stop itself;

        title = the title that is used while this is running.

        '''
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

    def progress(self, current, time_=None, tasksDone=0, pastBar=None):
        '''
        The loading bar itself

        # Params
        current = current percent of bar complete;


        # Optional Params
        time_ = how long its taken so far. Used for calculating eta;

        tasksDone = amount of tasks done, just for visualization;

        pastBar = used if you don't have threading, but want a nice animation to get to current percent;
        '''
        percent = float(current) * 100 / self.total
        bar = self.barChar * int(percent/100 * self.barLength - 1) + self.arrow
        spaces  = ' ' * (self.barLength - len(bar))
        space = ' ' * (5 - len(str(percent)))

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
        
        if pastBar != None:
            while len(bar) > pastBar:
                print('\t%s%s%s%s %s%d%s  [eta=%s] [tasks=%s/%s]' % (self.bracketChars[0], (self.barChar * pastBar), (spaces + (" " * (len(bar)-pastBar))), self.bracketChars[1], space, percent, self.percChar, eta, tasksDone, self.totalTasks), end='\r')
                pastBar += 1
                time.sleep(0.05)

            return len(bar)

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
        End bar.
        Shows full bar complete, and removes eta and shows all tasks complete (if any).

        # Optional Params
        tasks = optional param if you want to use external tasks
        '''
        bar  = self.barChar * self.barLength

        if tasks == None:
            total_tasks = self.totalTasks
        else:
            total_tasks = tasks

        print(f"\033[F{title}\t\t\t\t\t\t\t\t")

        if total_tasks == None:
            print(f'\t{self.bracketChars[0]}{bar}{self.bracketChars[1]} 100{self.percChar}')
        else:
            print(f'\t{self.bracketChars[0]}{bar}{self.bracketChars[1]} 100{self.percChar}  [tasks={total_tasks}/{total_tasks}]')



class SimulateTasks:
    '''Custom use of Bar() class.'''
    def __init__(self, eta=15, total=100, barLength=20):
        '''
        # Optional Params
        eta = Bar() eta param, most likely to be used of 3 optional params;

        total = total percent from Bar() class;

        barLength = Bar() barLength param;
        '''
        self.barLength = barLength
        self.eta = eta
        self.total = total
        self.simulateTasks
        self.simulateTasks()

    def simulateTasks(self):
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

        totaltime = time.time() - start_time
        total = 0
        lb.progress(total, totaltime)
        time.sleep(0.005*self.eta)
        totaltime = time.time() - start_time
        lb.progress(total+1, totaltime)

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

        time.sleep(0.1)
        lb.end((len(tasks)))

    def loadtasks(self):
        ntasks = random.randint(2, 5)
        tasks = []
        totalperc = self.total

        for i in range(ntasks):
            if ntasks == 1:
                j = 100
            else:
                j = random.randint(2, 6) * 10
                j *= (random.randint(95, 105) / 100)

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

        for i in range(len(tasks)):
            tasks[i] = round(tasks[i], 1)

        return tasks