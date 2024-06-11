"""Regular Queue

- implemented FIFO (First in First out) Principle
- Putting items in the queue: enqueue
- Removing items in the queue: dequeue
- Complexity: 0(1)

"""


class Queue:
    """Queue's class"""

    def __init__(self) -> None:
        self.__queue: list = []

    def queue(self):
        return self.__queue

    def check_empty(self):
        if len(self.__queue) == 0:
            return True
        return False

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        if self.check_empty():
            return None
        return self.__queue.pop(0)

    def display(self):
        print(self.__queue)

    def size(self):
        return len(self.__queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.display()
    queue.enqueue(2)
    queue.display()
    queue.enqueue(3)
    queue.display()
    queue.enqueue(4)

    queue.display()
    print("size: ", queue.size())

    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    print("size: ", queue.size())
