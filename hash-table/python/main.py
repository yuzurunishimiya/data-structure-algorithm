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

# Example by python (from programiz)

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    print(index)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = []

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)
