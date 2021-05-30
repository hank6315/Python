from random import randint
from os import getpid
from time import time, sleep


def download_task(filename):
    print('String Download Processing, pid[%d]' % getpid())
    print('Starting Downloading: %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download done ! time is : %d secs' % (filename, time_to_download))



def main():
    start = time()
    download_task('Hello.doc')
    download_task('test.mp3')
    end = time()
    print('Total time : %.2f secs.' % (end - start))


if __name__ == '__main__':
    main()