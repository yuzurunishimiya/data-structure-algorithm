"""
Linked List Singly is basically basic one:
    node -> node -> node
    :so the code actually not so much different with the basic one (or similar)
"""

from typing import Any


class Node:
    """node's class"""

    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def next_(self):
        """get node's next node"""

        return self.__next

    @next_.setter
    def next_(self, node):
        """set node's next node"""
        self.__next = node

    @property
    def data(self):
        """get node's data"""
        return self.__data

    @data.setter
    def data(self, new_data: Any):
        """set node's data"""

        self.__data = new_data


class SinglyLinkedList:
    """Singly Linked List's class"""

    def __init__(self, head: Node = None) -> None:
        self.__head = head

    @property
    def head(self):
        """get LL's head"""

        return self.__head

    @head.setter
    def head(self, head: Node):
        """set LL's head"""

        self.__head = head


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)

    # connect nodes
    one.next_ = two
    two.next_ = three

    # set head
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.head = one
