class CircularQueue:

    def __init__(self, max_size: int) -> None:
        self.__max_size = max_size
        self.__queue = [None] * self.__max_size
        self.__head = self.__tail = -1

    def enqueue(self, data):
        if ((self.__tail + 1) % self.__max_size == self.__head):
            print("\nThe circular queue is full\n")

        elif (self.__head == -1):
            self.__tail = 0
            self.__head = 0
            self.__queue[self.__tail] = data
        else:
            self.__tail = (self.__tail + 1) % self.__max_size
            self.__queue[self.__tail] = data

    def dequeue(self):
        if (self.__head == -1):
            print("\nqueue is empty\n")

        elif (self.__head == self.__tail):
            temp = self.__queue[self.__head]
            self.__head = -1
            self.__tail = -1
            return temp

        else:
            temp = self.__queue[self.__head]
            self.__head = (self.__head + 1) % self.__max_size
            return temp


    def printQueue(self):
        if (self.__head == -1):
            print("The circular queue is empty")

        elif (self.__tail >= self.__head):
            for i in range(self.__head, self.__tail + 1):
                print(self.__queue[i], end=" ")
            print()

        else:
            for i in range(self.__head, self.__max_size + 1):
                print(self.__queue[i], end=" ")
            for i in range(0, self.__tail + 1):
                print(self.__queue[i], end=" ")
            print()


if __name__ == "__main__":
    cq = CircularQueue(5)
    for i in range(1, 7):
        cq.enqueue(i)
        print("enqueue: ", i)
        print("The circular queue: ", end=" "); cq.printQueue()

    for _ in range(6):
        poped = cq.dequeue()
        print("dequeue: ", poped)
        print("The circular queue: ", end=" "); cq.printQueue()
