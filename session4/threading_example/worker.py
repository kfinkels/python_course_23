from threading import Thread
import time


def worker():
    print("Worker started")
    time.sleep(5)
    print("Worker finished")


if __name__ == '__main__':
    print("Main program started")
    t = Thread(target=worker)
    t.start()
    print("Main program continued running in background while the worker thread is busy doing its work")
    t.join()
    print("Main program finished")
