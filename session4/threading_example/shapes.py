import threading
import time


def print_cube():
    # function to print cube of given num
    while True:
        print("*****cube", end='\n')
        time.sleep(10)


def print_square():
    # function to print square of given num
    while True:
        print("square", end='\n')
        time.sleep(1)


if __name__ == '__main__':
    # creating thread
    t1 = threading.Thread(target=print_square, args=())
    t2 = threading.Thread(target=print_cube, args=())

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
