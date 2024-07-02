"""
Hash table:
    Sejauh yang saya mengerti hash table adalah ds untuk menyimpan data
    menggunakan pair key [key, data] kedalah sebuah table/array:
        di mana key merupakan "sesuatu" yang digunakan untuk membuka data
    namun demikian sejauh ini tidak diperlukan sebuah access key untuk menggukan fungsi hash
    biasanya dalam keamanan data, digunakan sebuah
        key+salt untuk mengakomodir ekskripsi dan deskripsi data

    -> key: unique integer that is used for indexing the values
    -> value: data that are associated with keys
    -> hashing func: h(k) -> h is hashing, k is key

Hash Collision:
    Terjadi ketika fungsi hash menggenerate index yang sama untuk multiple keys.
    (konflik) -> bisa dioverride atau menggunakan teknik:
        - Collision resolution by chaining
            yang berarti menyimpan data pada index yang sama dengan chain
            menggunakan sebuah doubly linked-list
            atau disimpan dalam bentuk array[tuple] -> [(),(),()...()]

            pseudocode:
                ChainedHashedSearch(T, k)
                    return T[h(k)]
                ChainedHashInsert(T, x):
                    T[h(x.key)] = x // insert at the head
                ChainedHashDelete(T, x):
                    T[h(x.key)] = NIL
        - Open Addressing
            i. Linear Probing (yang berarti increment by a constant)
                checking the next slot:
                    h(k, i) = (h'(k) + 1) % m
                        i = {0, 1, ...}
                        h'k(k): is the new hash function
                        m: size of table/bucket
            ii. Quadratic Probing
                checking by quadratic probing
                    h(k, i) = (h'(k) + c1i + c2i2) % m
                        c1 and c2 are positive auxiliary constants
                        i = {0, 1, ...}
            iii. Double Hashing
                jika slot pada hash pertama sudah terisi, maka akan dilakukan hash yang ke-2
                (dengan fungsi hash berbeda) untuk menemukan slot kosong.
                h(k, i) = (h1(k) + ih2(k)) % m

Good Hash Function
1. Division Method
    h(k) = k mod m
    h: function
    k: key
    m: size of table/bucket/list
    -> disarankan untuk tidak menggunakan m = 2^n karena:
        - akan menyebabkan banyak collision (small number of bucket)
        - poor distribution
        misal: m = 8 -> 2^3
                jika memiliki keys: 8, 16, 24, 32,... hash valuenya akan menjadi 0
                karena 8/16/24/32 % 8 = 0 menyebabkan menumpuknya data di index: 0
                maka m disarankan adalah nomor prima atau setidaknya bukan power of 2;
2. Multiplication Method
    h(k) = ⌊m(kA mod 1)⌋
        -> kA mod 1 gives fractional part kA
        -> ⌊ ⌋ give the floor value
        -> A is a constant, the value of A lies between 0 and 1. But, an optional choice will be
            ≈ (√5-1)/2 [suggested by Knuth]
3. Universal Hashing
    In Universal hashing, the hash function is chosen at random independent of keys.
"""

from typing import Any, Optional


class HashTable:
    """Hash table data structure"""

    def __init__(self, size: int) -> None:
        """size of array[], it will be good if it is a prime number"""
        self.__size = size
        self.__hash_table = [[],] * self.__size

    @staticmethod
    def check_prime(number) -> bool:
        """to check if number a prime number or not"""

        if number == 1 or number == 0:
            return False

        for i in range(2, number//2):
            if i % 2 == 0:
                return False

        return True

    def _hash_function_div_method(self, key) -> int:
        """division method hash function"""

        return key % self.__size

    def insert_data(self, key, data) -> None:
        """insert data"""

        # ignore collision
        index = self._hash_function_div_method(key)
        self.__hash_table[index] = [key, data]

        # use chaining to solve collision
        # index = self._hash_function_div_method(key)
        # self.__hash_table[index].append((key, data,))

    def lookup_data(self, key) -> Optional[Any]:
        """to look up data"""

        # ignore collision, so data maybe overwritted (will be not found)
        index = self._hash_function_div_method(key)
        target = self.__hash_table[index]

        # target[0] => key, target[1] => data
        if target[0] == key:
            return target[1]

        # if chaining method used
        # index = self._hash_function_div_method(key)
        # target = self.__hash_table[index]

        # target[] -> [(),(),(), ...] -> (): container
        # container[0] = key, container[1] = data

        # for container in target:
        #     if container[0] == key:
        #         return container[1]

    def remove_data(self, key) -> None:
        """to remove data"""

        index = self._hash_function_div_method(key)
        self.__hash_table[index] = []

        # if chaining method used
        # index = self._hash_function_div_method(key)
        # target = self.__hash_table[index]
        # container_index = None
        # for i, container in enumerate(target):
        #     if container[0] == key:
        #         container_index = i
        #         break

        # if container_index:
        #     target.pop(container_index)

    def display_hash_table(self):
        """to display hash table"""

        print(self.__hash_table)


if __name__ == "__main__":
    ht = HashTable(7)
    ht.insert_data(key=123, data="apple")
    ht.insert_data(key=234, data="orange")
    ht.insert_data(key=345, data="banana")

    ht.display_hash_table()
    KEY = 123
    lookup = ht.lookup_data(KEY)
    print(f"lookup data of key {KEY}: {lookup}")

    ht.remove_data(345)
    ht.display_hash_table()
