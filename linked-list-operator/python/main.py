# linked list operator
# 1. Traversal
# 2. Insertion
# 3. Deletion
# 4. Search
# 5. Sort


from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self) -> None:
        self.__head: Node = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value: Node):
        self.__head = value

    def insert_at_beginning(self, data: Any):
        new_node = Node(data)
        new_node.next = self.__head
        self.head = new_node

    def insert_after(self, previous_node: Any, new_data: Any):
        if previous_node is None:
            print("The given previous node must be in LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def insert_at_end(self, new_data: Any):
        new_node = Node(new_data)

        if self.__head is None:
            self.__head = new_node
            return

        last = self.__head
        while(last.next):
            last = last.next

        last.next = new_node
