from multiprocessing import Process
from os import getpid
from threading import Thread, Lock
from random import randint
from time import time, sleep

def download_task(filename):
    # print('start process, number [%d]' % getpid())
    print('start downloading %s ' %filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finished, takes %d seconds' %(filename, time_to_download))


def main_process():
    start = time()
    p1 = Process(target=download_task, args=('Pythom.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('total takes %.2f seconds.' %(end-start))


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('start downloading %s ' %self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s download finished, takes %d seconds' %(self._filename, time_to_download))


def main_Thread():
    start = time()
    #p1 = Thread(target=download_task, args=('Pythom.pdf', ))
    p1 = DownloadTask('python.pdf')
    p1.start()
    #p2 = Thread(target=download_task, args=('Peking.avi', ))
    p2 = DownloadTask('Peking.avi')
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('total takes %.2f seconds.' %(end-start))


# saving money
class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main_deposit():
    account = Account()
    threads =[]
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print('account money: %d' %account.balance)


# Study Case 1 : Coroutine with download procedure
import time
import tkinter
import tkinter.messagebox

def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('Tips', 'Finish downloading.')

def show_about():
    tkinter.messagebox.showinfo('About', 'Author: ryan')

def main_coroutine():
    
    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('tips', 'Finish download!')
            btn1.config(state=tkinter.NORMAL)

    def download():
        btn1.config(state=tkinter.DISABLED)
        DownloadTaskHandler(daemon=True).start()


    top = tkinter.Tk()
    top.title('Single Thread')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    btn1 = tkinter.Button(panel, text='Download', command=download)
    btn1.pack(side='left')

    btn2 = tkinter.Button(panel, text='About', command=show_about)
    btn2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


# Study Case 2 : Divide and Conqure
from time import time
from multiprocessing import Process, Queue

def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handler, 
            args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Excution time: %.3fs' %(end-start))



if __name__ == '__main__':
    main()