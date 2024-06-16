"""
Linked List Operations:
    - Traversal
        access each element of the LL
    - Insertion
        add new element to LL
    - Deletion
        removes the existing elements
    - Search
        find a node in a LL
    - Sort
        sort the nodes of the LL

Things to remember:
    - head: points to the the first node of LL
    - next-pointer of the last is null, so if (next == null)
        we have reached the end of the LL

"""

from typing import Any
from typing import Optional
from random import choice


class Node:
    """Linked List Node's class
    
    why using getter and setter?
    - to encapsulate (even tho python has no specific keyword to encapsulate)
    - validate and logic: add extra validate and logic to setter
    - flexibility
    - interface consistency

    """

    def __init__(self, data: Any) -> None:
        self.__data = data # data belongs to node
        self.__next = None # next linked list node

    @property
    def data(self):
        """get node's data"""

        return self.__data

    @data.setter
    def data(self, val: Any):
        """to set node's data

        val: value
        value type: any primitif types
        """

        self.__data = val

    @property
    def next(self):
        """get next node"""

        return self.__next

    @next.setter
    def next(self, next_node: 'Node'):
        """to set next node"""

        if not isinstance(next_node, Node):
            print("invalid value of next_node, Node object expected")
        else:
            self.__next = next_node

class LinkedList:
    """Linked List's class"""

    def __init__(self, head_node: Optional[Node] = None) -> None:
        self.__head = head_node

    @property
    def head(self):
        """get Linked List's head"""

        return self.__head

    @head.setter
    def head(self, node: Node) -> None:
        """set head's value

        node: Node you want to set as a head of linked list
        type value: Node object

        :return None
        """

        if not isinstance(node, Node):
            print("head node must be a node type")
        else:
            self.__head = node

    def insert_at_beginning(self, data: Any) -> None:
        """to insert data to head"""

        # -> create new node
        # -> set current head node as next node (to new node)
        # -> set new node as new head of LL

        new_node = Node(data)
        new_node.next = self.__head
        self.head = new_node

    def insert_after(self, previous_node: Node, new_node_data: Any) -> None:
        """to create new node + insert new data to next node"""

        if not isinstance(previous_node, Node):
            print("previous node must be a node object")

        new_node = Node(new_node_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def insert_at_end(self, new_node_data: Any) -> None:
        """to insert node at the end of the LL"""

        new_node = Node(new_node_data)
        if self.__head is None:
            self.__head = new_node
        else:
            # get head -> travelsal to the end of the node (null next == last node)
            last = self.__head
            while last.next: # if last != null; then its not the end
                last = last.next

            last.next = new_node

    def delete_node(self, position: int) -> Optional[Node]:
        """to delete node at specific position
        position based on array index (start from 0);

        position: position of node to delete
        type: integer >= 0
        """

        if position < 0:
            print("position must be a positive number")
        elif self.__head is None:
            return
        elif position == 0:
            temp = self.__head
            self.__head = temp.next
            return temp
        else:
            cur = self.__head
            for _ in range(position - 1):
                cur = cur.next
                if cur is None: # cur None means position is higher than ll length
                    break

        if cur is None or cur.next is None:
            print("position is higher than linked list length!")
            return

        # this current next is position - 1; so if we want to delete position 2
        # the current is 1; so cur.next > 2.node > 3.node so next(2).next(3); 1 - 2 - 3 -> 1 - 3
        temp = cur.next
        cur.next = cur.next.next

        return temp

    def search(self, key) -> Optional[Node]:
        """to search based on data/key"""

        cur = self.__head
        while cur.next:
            if cur.data == key:
                return cur

            cur = cur.next

    def sort(self, reversed_sort: bool = False):
        """to sort"""

        cur = self.__head
        idx = Node(None)

        if cur is None:
            return

        # karena ditambahkan percabangan if reversed_sort
        # untuk mendapatkan runtime yang lebih baik maka harus duplikat code dibawah
        # dan mengganti if reversed_sort menjadi < dan > pada kedua kode
        # maka digunakan percabangan karena perbedaan runtime pada angka data dibawah 20k
        # masih menghasilkan runtime yang cenderung sama/tidak begitu berbeda jauh hasilnya

        while cur is not None:
            idx: Node = cur.next # idx = next node

            while idx is not None:
                if reversed_sort is False:
                    if cur.data > idx.data:
                        cur.data, idx.data = idx.data, cur.data
                else:
                    if cur.data < idx.data:
                        cur.data, idx.data = idx.data, cur.data

                idx = idx.next

            cur = cur.next

    def print_list(self) -> None:
        """print linked-list"""

        node = self.__head
        while node is not None:
            print(f"{node.data} ", end=" ")
            node = node.next

        print() # to the grand line


if __name__ == "__main__":
    numbers = [x for x in range(1, 100)]
    arr_pop = [choice(numbers) for _ in range(10)]

    head = Node(0)
    linked_list = LinkedList(head)

    k = linked_list.head
    for item in arr_pop:
        nn = Node(item)
        k.next = nn
        k = nn

    linked_list.print_list()
    linked_list.sort()
    linked_list.print_list()
    linked_list.delete_node(5)
    linked_list.print_list()
    linked_list.insert_at_beginning(-10)
    linked_list.print_list()
    searched_node = linked_list.search(-10)
    print("searced_node: ", searched_node.data)
    linked_list.insert_after(searched_node, new_node_data=-1)
    linked_list.print_list()
    searched_node = linked_list.search(-210)
    print("searced_node: ", searched_node.data if searched_node is not None else "not find")
