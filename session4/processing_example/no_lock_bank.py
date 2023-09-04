import multiprocessing
import time


def deposit(balance):
    for i in range(500):
        time.sleep(0.1)
        balance.value = balance.value + 1


def withdraw(balance):
    for i in range(500):
        time.sleep(0.1)
        balance.value = balance.value - 1


if __name__ == '__main__':
    # Create a shared memory
    balance = multiprocessing.Value('i', 500)
    p1 = multiprocessing.Process(target=deposit, args=(balance,))
    p2 = multiprocessing.Process(target=withdraw, args=(balance,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(balance.value)


