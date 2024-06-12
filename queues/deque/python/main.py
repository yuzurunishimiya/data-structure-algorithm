"""
Deque: Double Ended Queue
    - Insertion/Removal of elements can be performed from the front or the rear
    - Doesn't follow FIFO Rules
Types:
    - Input Restricted Deque: input single, delete both ends
    - OUtput Restricted Deque: input both ends, delete single

    Below is Circular Array Implementation of Deque
"""

from typing import Any, List
from typing import Literal, Optional

import random


class Deque:
    """Dequeue (Dynamic/non-strict/unfixed size)"""

    def __init__(self) -> None:
        self.__items = []

    def is_empty(self):
        """check if empty"""
        return not self.__items

    def add_rear(self, item: Any):
        """add item to rear of queue"""
        self.__items.append(item)

    def add_front(self, item: Any):
        """add item to front of queue"""
        self.__items.insert(0, item)

    def remove_front(self):
        """remove item from front of queue"""
        if len(self.__items) > 0:
            return self.__items.pop(0)
        return None

    def remove_rear(self):
        """remove item from rear of queue"""
        if len(self.__items) > 0:
            return self.__items.pop()
        return None

    def size(self):
        """get size of queue"""
        return len(self.__items)


class DequeQueue:
    """Double ended queue's class"""

    def __init__(self, max_size: int) -> None:
        self.__max_size: int = max_size
        self.__queue: List[Any] = [None] * max_size
        self.__front: int = -1
        self.__rear: int = -1

    def check_full(self) -> bool:
        """check if queue is full"""

        return (
            (self.__front == 0 and self.__rear == self.__max_size - 1)
            or
            (self.__front == self.__rear + 1)
        )

    def check_empty(self) -> bool:
        """check if queue is empty"""

        return self.__front == -1

    def set_front_rear(self, val: int):
        """to set front and rear if queue is empty when insert"""

        self.__front = val
        self.__rear = val

    def insert_front(self, item: Any) -> None:
        """insert item/element from front of queue"""

        if self.check_full():
            print("Queue is Full!")
        else:
            if self.check_empty():
                self.set_front_rear(0)
            elif self.__front < 1:
                self.__front = self.__max_size - 1
            else:
                self.__front = self.__front - 1

            self.__queue[self.__front] = item

    def insert_rear(self, item: Any) -> None:
        """insert item/element from rear of the queue"""

        if self.check_full():
            print("Queue is full!")
        else:
            if self.check_empty():
                self.set_front_rear(0)
            elif self.__rear == self.__max_size -1:
                self.__rear = 0
            else:
                self.__rear = self.__rear + 1

            self.__queue[self.__rear] = item

    def delete_front(self) -> Optional[Any]:
        """delete item/element from front of the queue"""

        if self.check_empty():
            print("Queue is empty!")
            return None

        popped_item = self.__queue[self.__front]
        self.__queue[self.__front] = None # biar keliatan aja di print, jd di set none

        if self.__front == self.__rear: # last element
            self.set_front_rear(-1)

        elif self.__front == self.__max_size - 1:
            self.__front = 0
        else:
            self.__front = self.__front + 1

        return popped_item

    def delete_rear(self) -> Optional[Any]:
        """delete item/element from rear of the queue"""

        if self.check_empty():
            print("Queue is empty")
            return None

        popped_item = self.__queue[self.__rear]
        self.__queue[self.__rear] = None # biar keliatan aja di print, jd di set none

        if self.__rear == self.__front: # last element
            self.set_front_rear(-1)

        elif self.__rear == 0:
            self.__rear = self.__max_size - 1
        else:
            self.__rear = self.__rear - 1

        return popped_item

    def display_queue(self) -> None:
        """display queue"""

        print(self.__queue)

    def display_items(self, direction: Literal[-1, 1] = 1) -> None:
        """display items or elements of queue
        
        :q direction: Literal[-1, 1]: -1 from rear to front, 1 from front to rear
        :return None
        """

        if self.check_empty():
            print("Queue is empty!")

        if direction > 0:
            if self.__rear >= self.__front:
                for index in range(self.__front, self.__rear + 1):
                    print(self.__queue[index], end=" ")
            else:
                for index in range(self.__front, self.__max_size):
                    print(self.__queue[index], end=" ")
                for index in range(self.__rear + 1):
                    print(self.__queue[index], end=" ")
        else:
            if self.__rear >= self.__front:
                for index in range(self.__rear, self.__front -1, -1):
                    print(self.__queue[index], end=" ")
            else:
                for index in range(self.__rear, -1, -1):
                    print(self.__queue[index], end=" ")
                for index in range(self.__max_size - 1, self.__front - 1, -1):
                    print(self.__queue[index], end=" ")


class InsertPopQueueTesting:
    """To insert and pop queue for testing"""

    @staticmethod
    def insert(queue_: DequeQueue, length: int, fr: Literal['f', 'r']):
        """to insert item"""

        if fr == 'f':
            insert = queue_.insert_front
        else:
            insert = queue_.insert_rear

        for number in range(length):
            print(" --- ")
            number = str(number + random.choice([10,20,30,40,50,60,70,80,90])) # biar random aja
            print(f"trying to enqueue [f/r: {fr}] item: ", number)
            insert(item=number)
            print("queue: ", end=" ")
            queue_.display_queue()
            print(" --- ")

    @staticmethod
    def pop(queue_: DequeQueue, length: int, fr: Literal['f', 'r']):
        """to pop item"""

        if fr == 'f':
            pop = queue_.delete_front
        else:
            pop = queue_.delete_rear

        for _ in range(length):
            print(" --- ")
            popped_item = pop()
            print(f"popped item[f/r: {fr}]: ", popped_item)
            print("queue: ", end=" ")
            queue_.display_queue()
            print(" --- ")


if __name__ == '__main__':

    print(" --- old code log ---")
    d = Deque()
    d.add_rear(1)
    d.add_rear(2)
    d.add_front(0)
    d.add_front(-1)

    print("size: ", d.size())
    print("is empty: ", d.is_empty())
    print(" --- end of old code log ---")

    print(" --- new code log ---")

    deque = DequeQueue(max_size=6)
    tdq = InsertPopQueueTesting()
    tdq.insert(deque, 2, 'f')
    tdq.insert(deque, 1, 'r')
    tdq.pop(deque, 1, 'f')
    tdq.insert(deque, 3, 'r')
    tdq.pop(deque, 2, 'r')
    tdq.pop(deque, 2, 'f')
    tdq.insert(deque, 8, 'f')
    tdq.pop(deque, 7, 'f')
    tdq.insert(deque, 1, 'f')

    print(" --- end of new code log ---")
