"""Linked List [Circular type]
    Tipe data yang men-link tapi circular
        A -> B -> C -> ...-> (n) -> A

- Create Nodes
- Connect nodes
    Node x <- Node y <- Node ... <- Node n
- Set Nodes' Head

"""

from typing import Any


class Node:
    """Node Class [Sebuah konstruksi node]"""

    def __init__(self, data) -> None:
        # 2 fields yaitu data, dan next node yang me-link
        # encapsulate the data but allow set next via method
        self.__data = data
        self.__next = None

    @property
    def next_node(self):
        """get next node data"""

        return self.__next

    @next_node.setter
    def next_node(self, node):
        """a method to set a next node"""

        self.__next = node

    @property
    def data(self):
        """get data"""

        return self.__data

    @data.setter
    def data(self, value: Any):
        """set data"""

        # you can add a logic or validation before assign the value
        # below here
        self.__data = value


class CircularLinkedList:
    """Circular Linked List Class [Konstruksi yang mengatur linked list]"""

    def __init__(self, head: Node = None) -> None:
        self.__head = head

    @property
    def head(self):
        """get nodes' head"""
        return self.__head

    @head.setter
    def head(self, head: Node):
        """to set head (a node class) to the circular linked list"""
        self.__head = head

    def insert_at_beginning(self, new_data: Any) -> None:
        """to insert at beginning of LL"""

        new_node = Node(new_data)

        if self.__head is None:
            pass
        elif self.__head.next_node is None:
            self.__head.next_node = new_node
            new_node.next_node = self.__head
        else:
            last_node = self.__head
            while last_node.next_node is not self.__head:
                last_node = last_node.next_node

            last_node.next_node = new_node
            new_node.next_node = self.__head

        self.__head = new_node

    def insert_after(self, previous_node: Node, new_node_data: Any) -> None:
        """to create new node + insert new data to next node"""

        new_node = Node(new_node_data)
        if self.__head is None:
            self.__head = new_node
        elif previous_node is self.__head:
            self.__head.next_node = new_node
            new_node.next_node = self.__head
        else:
            new_node.next_node = previous_node.next_node
            previous_node.next_node = new_node

    def insert_at_end(self, new_node_data: Any) -> None:
        """to creat new node + insert node in the end of node"""

        new_node = Node(new_node_data)
        if self.__head is None:
            self.__head = new_node
        else:
            last_node = self.__head
            while last_node and last_node.next_node is not self.__head:
                last_node = last_node.next_node

            last_node.next_node = new_node
            new_node.next_node = self.__head

    def print_list(self) -> None:
        """print linked list"""

        node = self.__head

        while node:
            print(f"{node.data}", end=", ")
            node: Node = node.next_node
            if node is self.__head:
                print("reached the last node a.k.a head of LL, val: ", node.data, end=" ")
                break
        else:
            print("next-node is null (head only)", end=".")

        print() # to the grand line


if __name__ == "__main__":
    print(" --- start --- ")
    ll = CircularLinkedList()
    ll.insert_at_beginning(10)
    ll.print_list()
    ll.insert_at_beginning(9)
    ll.print_list()
    ll.insert_at_end(11)
    ll.print_list()
    ll.insert_at_beginning(0)
    ll.print_list()
    print(" --- end --- ")
