"""
Linked List:
    linear data structure that include a series of connected nodes.
    Head -> [data|next] -> [data|next] -> Null
    types:
        - singly
        - doubly
        - circular
    Application:
        - Dynamic memory allocation
        - Implemented in stack and queue
        - In Undo function of sofwares
        - Hash tables, graphs

    This One Below is singly
"""

from typing import Any, Optional


class Node:
    """Node's class"""

    def __init__(self, data: Optional[Any] = None) -> None:
        self.__data: Any = data
        self.__next: __class__ = None

    @property
    def next(self):
        """get next node"""

        return self.__next

    @next.setter
    def next(self, value: Any):
        """set next node"""

        self.__next = value

    @property
    def data(self) -> Any:
        """get data"""

        return self.__data

    @data.setter
    def data(self, val: Any) -> None:
        """set data"""

        self.__data = val


class LinkedList:
    """Linked List's class"""

    def __init__(self, head: Optional[Node] = None) -> None:
        self.__head = head

    @property
    def head(self):
        """get head"""

        return self.__head

    @head.setter
    def head(self, value: Node):
        """set nead"""

        self.__head = value


if __name__ == '__main__':

    linked_list = LinkedList()

    # assign item value
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # connect nodes
    linked_list.head.next = second
    second.next = third

    # print
    next_nodes: Node = linked_list.head
    while next_nodes is not None:
        print(next_nodes.data, end=" ")
        next_nodes = next_nodes.next
