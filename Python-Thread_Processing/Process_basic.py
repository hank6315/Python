from random import randint
from os import getpid
from time import time, sleep
from multiprocessing import Process


def download_task(filename):
    print('String Download Processing, pid[%d]' % getpid())
    print('Starting Downloading: %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download done ! time is : %d secs' % (filename, time_to_download))

#by processing
def main():
    start = time()
    p1 = Process(target=download_task , args=('Hello.doc', ))
    p2 = Process(target=download_task , args=('test.mp3', ))

    p1.start()
    p1.join()
    p2.start()
    p2.join()  
    end = time()

    print('Total time : %.2f secs.' % (end - start))


if __name__ == '__main__':
    main()