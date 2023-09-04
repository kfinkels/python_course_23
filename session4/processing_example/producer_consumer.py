from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Queue


def producer(queue):
    print('Producer: Running', flush=True)
    for i in range(10):
        # generate a value
        value = random()
        sleep(value)
        # add to the queue
        queue.put(value)
        print(f'>>put {value}', flush=True)
    # this will stop the example
    queue.put(None)
    print('Producer: Done', flush=True)


# consume work
def consumer(queue):
    print('Consumer: Running', flush=True)
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            break
        print(f'>got {item}', flush=True)
    print('Consumer: Done', flush=True)


if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # start the consumer
    consumer_process = Process(target=consumer, args=(queue,))
    consumer_process.start()
    # start the producer
    producer_process = Process(target=producer, args=(queue,))
    producer_process.start()
    # wait for all processes to finish
    producer_process.join()
    consumer_process.join()
