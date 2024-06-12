"""Regular Queue

- implemented FIFO (First in First out) Principle
- Putting items in the queue: enqueue
- Removing items in the queue: dequeue
- Complexity: 0(1)

"""

from typing import Any


class Queue:
    """Queue's class
    This queue is not use head/tail index
    """

    def __init__(self) -> None:
        self.__queue: list = []

    def check_empty(self):
        """to check if queue empty"""
        if len(self.__queue) == 0:
            return True
        return False

    def enqueue(self, item):
        """to enqueue/insert item to queue"""
        self.__queue.append(item)

    def dequeue(self):
        """to dequeue/pop item from queue"""
        if self.check_empty():
            return None
        return self.__queue.pop(0)

    def display(self):
        """to display queue"""
        print(self.__queue)

    def size(self):
        """to get length of queue"""
        return len(self.__queue)


class RegularQueue:
    """new regular queue's class"""

    def __init__(self, max_size: int) -> None:
        self.__max_size = max_size
        self.__queue = [None] * max_size
        self.__head = self.__tail = -1

    def enqueue(self, item: Any) -> None:
        """to enqueue/insert item to queue"""

        if self.__tail == -1:
            self.__head = 0
            self.__tail = 0
            self.__queue[self.__tail] = item
            print("enqueue new item successfully, item: ", item)

        elif (self.__tail + 1) % self.__max_size == 0:
            print("Queue is full!")

        else:
            self.__tail += 1
            self.__queue[self.__tail] = item
            print("enqueue new item successfully, item: ", item)


    def dequeue(self) -> Any:
        """to deqeue/pop item from queue"""

        if self.__head == -1:
            print("Queue is empty!")

        # last element
        elif (self.__head + 1) % self.__max_size == 0:
            popped_item = self.__queue[self.__head]
            self.__head = -1
            self.__tail = -1
            self.__queue[self.__head] = None # reset to None, bisa di ignore si sebenernya
            return popped_item

        else:
            popped_item = self.__queue[self.__head]
            self.__queue[self.__head] = None
            self.__head += 1
            return popped_item

    def display_queue(self) -> None:
        """to display queue"""

        print(self.__queue)

    def display_queue_items(self) -> None:
        """to display queue items (secara berurutan)"""

        if self.__head == -1:
            print("Queue is empty!")
        else:
            for index in range(self.__head, self.__max_size):
                print(self.__queue[index], end=" ")


class InsertPopQueueTesting:
    """To insert and pop queue for testing"""

    @staticmethod
    def insert(queue_: RegularQueue, length: int):
        """to insert"""

        for number in range(length):
            print(" --- ")
            number = number + 10 # biar +10 aja
            print("trying enqueue new item: ", number)
            queue_.enqueue(item=str(number))
            print("queue: ", end=" ")
            queue_.display_queue()
            print("queue items: ", end=" ")
            queue_.display_queue_items()
            print()
            print(" --- ")

    @staticmethod
    def pop(queue_: RegularQueue, length: int):
        """to insert"""

        for _ in range(length):
            print(" --- ")
            popped_item = queue_.dequeue()
            print("popped item: ", popped_item)
            print("queue: ", end=" ")
            queue_.display_queue()
            print("queue items: ", end=" ")
            queue_.display_queue_items()
            print(" --- ")


if __name__ == "__main__":
    print(" --- old queue code log ---")
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

    print(" --- end of old queue code log ---")

    print(" --- new regular queue code log ---")
    regular_queue = RegularQueue(max_size=5)
    trq = InsertPopQueueTesting()
    trq.insert(regular_queue, 6)
    trq.pop(regular_queue, 2)
    trq.insert(regular_queue, 2)
    trq.pop(regular_queue, 6)
    trq.insert(regular_queue, 3)
    trq.pop(regular_queue, 2)
    trq.insert(regular_queue, 1)
    trq.pop(regular_queue, 2)
    print(" --- end of new regular queue code log ---")
