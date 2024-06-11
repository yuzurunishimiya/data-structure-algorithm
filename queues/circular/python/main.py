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


def insert_item_test(queue_obj: object, size: int):
    """untuk test insert"""
    for item in range(size): # 0 - 6, untuk cek jika queue full
        queue_obj.enqueue(str(item + 10)) # sengaja kita set item+10 (chg to string juga)
        print(f"enqueue new item: {item + 10}")

        print("queue-list-type:", end=" ")
        queue_obj.print_queue()

        print("queue:", end=" ")
        queue_obj.print_queue_old()

        print()
        print("--- ---")


def pop_item_test(queue_obj: object, size: int):
    """untuk test dequeue"""
    for _ in range(size):
        popped = queue_obj.dequeue()
        print("dequeue item: ", popped)

        print("queue-list-type:", end=" ")
        queue_obj.print_queue()

        print("queue:", end=" ")
        queue_obj.print_queue_old()

        print()
        print("--- ---")


if __name__ == "__main__":
    # testing

    circular_queue = CircularQueue(max_size=5)
    insert_item_test(circular_queue, 7) # dibuat lebih dari max-size untuk test
    pop_item_test(circular_queue, 3)
    insert_item_test(circular_queue, 2)
    pop_item_test(circular_queue, 5)
