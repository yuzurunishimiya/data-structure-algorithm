"""Circular Queue

- Extended version of regular queue
- The last element of queue connected to the first element
- Solves the major limitation of the normal queue.
    -> normal queue
        [space0, space1, x, y, z] -> x: front, z: rear
            -> tidak dapat insert dibelakang z (harus kosong dulu)
    -> circular queue
        [space0, space1, x, y, z] -> x: front, z: rear
            -> space0 akan diisi dengan data baru + menjadi rear baru (bukan z lagi)

- Enque & Deque Operation
    -> Enque
        - cek queue full/tidak
        - untuk item pertama, set value ke 0
        - menambahkan rear index + 1 secara sirkular (jika full, maka akan ke index awal)
        - menambahkan elementnya ke posisi yang ditunjukkan oleh rear
    -> Deque
        - cek jika queue kosong
        - me-return data yang ditunjukkan oleh front
        - menambahkan front index + 1 secara sirkular (jika full, maka akan ke index awal)
        - jika item adalah item terakhir dalam queue,
            maka setelah item dikeluarkan set head dan rear ke -1

    check for full queue:
        - front = 0 && rear = size - 1;
            misal [None]*3 -> [1,2,3]
            front (index 0) = 1, rear index size(3) - 1 (index 2) = 3, yang berarti queue full
        - front = rear + 1
            misal [None]*3 -> [1,2,3]
            rear (index 1) = 2, front = rear + 1 = 2; yang berarti -> [1(rear), 2(head), 3]
"""

class CircularQueue:
    """Circular Queue Class"""

    def __init__(self, max_size: int) -> None:
        self.__max_size = max_size
        self.__queue = [None] * max_size
        self.__head = self.__tail = -1

    def enqueue(self, data):
        """enqueue/menambah data"""

        # check if queue is full
        # misal index -> 0,1,2,3,4 (array size = 5). jika real + 1 == head berarti kan full.
        # pake modulus krn jk rear = 4 (head di 0), maka 4+1 akan 5 bukan 0. (tail + 1) % max-size
        # itu nilainya selalu dibawah nilai max-sizenya. misal 1%5 = 1, 2%5=2, dan 5%5 = 0
        # ini juga karena sistem circular, jika head di 3 dan tail di 2 (yang berarti full); maka
        # (2 + 1) % 5 = 3 (sama dengan head -> Full)

        if (self.__tail + 1) % self.__max_size == self.__head:
            print("The circular queue is full!")

        elif self.__head == -1:
            self.__tail = 0
            self.__head = 0
            self.__queue[self.__tail] = data
        else:
            self.__tail = (self.__tail + 1) % self.__max_size
            self.__queue[self.__tail] = data

    def dequeue(self):
        """dequeue / mengeluarkan data"""

        # if head = -1 berarti data kosong, karena ketika dequeue last item di set head = -1
        if self.__head == -1:
            print("queue is empty!")

        # jika head = tail, ini berarti last item dalam queue
        # akan menset head dan tail = -1 (queue kosong)
        elif self.__head == self.__tail:
            temp = self.__queue[self.__head]
            self.__queue[self.__head] = None # opsional, dibiarkan ada isinya juga gpp
            self.__head = -1
            self.__tail = -1
            return temp

        # jika item > 1; maka get item ke dalam temporary variable (item pada head)
        # set head ke + 1; jika head di last index -> set ke 0, untuk itulah digunakan modulus
        # (head + 1) % max-size. ex: head 4, max-size 5 -> (4 + 1) % 5 = 0
        # akan set ke 0 (head yang baru)
        # namun jika bukan di last index, misal head 3 -> (3 + 1) % 5 = 4, head akan jadi 4
        else:
            temp = self.__queue[self.__head]
            self.__queue[self.__head] = None # opsional, dibiarkan ada isinya juga gpp
            self.__head = (self.__head + 1) % self.__max_size
            return temp

    def print_queue(self):
        """to print queue"""

        print(self.__queue)

    def print_queue_old(self):
        """to print queue"""

        if self.__head == -1:
            print("The circular queue is empty")

        elif self.__tail >= self.__head:
            for index in range(self.__head, self.__tail + 1):
                print(self.__queue[index], end=" ")

        else:
            for index in range(self.__head, self.__max_size):
                print(self.__queue[index], end=" ")
            for index in range(self.__tail + 1):
                print(self.__queue[index], end=" ")


class Testing:
    """Testing Circular Queue"""

    def __init__(self, tested_class: CircularQueue) -> None:
        self.__uniq_incr: int = 9
        self.__queue_obj: CircularQueue = tested_class


    def _dispay(self) -> None:
        """doc here..."""

        print("queue: ", end=" ")
        self.__queue_obj.print_queue()
        print("queue items: ", end=" ")
        self.__queue_obj.print_queue_old()
        print()

    def insert(self, length: int) -> None:
        """to insert item/element to queue"""

        for _ in range(length):
            self.__uniq_incr += 1
            print(" --- ")
            print("trying enqueue new item: ", self.__uniq_incr)
            self.__queue_obj.enqueue(self.__uniq_incr)
            self._dispay()
            print()
            print(" --- ")

    def pop(self, length: int):
        """to pop item/element from queue"""

        for _ in range(length):
            print(" --- ")
            popped_item = self.__queue_obj.dequeue()
            print("popped item: ", popped_item)
            self._dispay()
            print(" --- ")


if __name__ == "__main__":
    # testing

    circular_queue = CircularQueue(max_size=5)
    tcq = Testing(circular_queue)
    tcq.insert(7)
    tcq.pop(3)
    tcq.insert(2)
    tcq.pop(5)
    tcq.insert(1)
    tcq.pop(1)
    tcq.insert(3)
    tcq.insert(1)
    tcq.pop(2)
    tcq.insert(1)
    tcq.insert(2)
    tcq.pop(2)
