from random import randint
from os import getpid
from time import time, sleep
from threading import Thread,Lock

database_value = 0

def increase(lock):
    global database_value

    lock.acquire()
    local_copy = database_value

    local_copy += 1
    sleep(0.01)
    database_value = local_copy
    lock.release()


def main():

    lock = Lock()
    print('start value', database_value)
    p1 = Thread(target=increase, args=(lock, ))
    p2 = Thread(target=increase, args=(lock, ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print('end value', database_value)
    



if __name__ == '__main__':
    main()