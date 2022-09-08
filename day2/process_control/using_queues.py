import multiprocessing
import random
import time


class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.random()
            self.queue.put(item)
            print(f"Producer: putting {item}")
            time.sleep(1)


class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("Finished!")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f"Consumer: getting {item}")
                time.sleep(1)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
