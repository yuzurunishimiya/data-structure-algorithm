class Node:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def _next(self):
        return self.__next

    @_next.setter
    def _next(self, node):
        self.__next = node

    @property
    def data(self):
        return self.__data


class SinglyLinkedList:
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

    # connect nodes
    one._next = two
    two._next = three

    # set head
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.head = one
