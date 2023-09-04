import multiprocessing
import time


def deposit(balance, lock):
    for i in range(500):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance, lock):
    for i in range(500):
        time.sleep(0.1)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


if __name__ == '__main__':
    # Create a shared memory
    balance = multiprocessing.Value('i', 500)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit, args=(balance, lock))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(balance.value)


