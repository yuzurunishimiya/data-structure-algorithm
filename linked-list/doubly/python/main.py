class Node:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def _next(self):
        return self.__next

    @_next.setter
    def _next(self, node):
        self.__next = node

    @property
    def _prev(self):
        return self.__prev

    @_prev.setter
    def _prev(self, prev):
        self.__prev = prev

    @property
    def data(self):
        return self.__data


class DoublyLinkedList:
    def __init__(self, head: Node = None) -> None:
        self.__head = head

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head: Node):
        self.__head = head


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)

    # connect nodes circular
    one._next = two
    one._prev = None

    two._next = three
    two._prev = one

    three._next = None
    three._prev = two

    # set head
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.head = one
