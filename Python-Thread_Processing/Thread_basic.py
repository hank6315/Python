from random import randint
from os import getpid
from time import time, sleep
from threading import Thread

def download_task(filename):
    print('String Download Thread, pid[%d]' % getpid())
    print('Starting Downloading: %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download done ! time is : %d secs' % (filename, time_to_download))


def main():
    start = time()
    p1 = Thread(target=download_task , args=('Hello.doc', ))
    p2 = Thread(target=download_task , args=('test.mp3', ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()

    print('Total thread time : %.2f secs.' % (end - start))



if __name__ == '__main__':
    main()