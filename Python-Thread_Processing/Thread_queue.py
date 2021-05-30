
from threading import Thread, current_thread,Lock
from queue import Queue

database_value = 0

def worker(q,lock):
    while True:
        value = q.get()
        #prosessing 
        with lock:
            print(f'in {current_thread().name} get {value}')
        q.task_done()
       
def main():

    lock = Lock()
    q = Queue()
    num_threads = 3

    for i in range(num_threads):
        thread = Thread(target=worker , args=(q,lock, ))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

if __name__ == '__main__':
    main()