"""Linked List [Circular type]
    Tipe data yang men-link tapi circular
        A -> B -> C -> ...-> (n) -> A

- Create Nodes
- Connect nodes
    Node x <- Node y <- Node ... <- Node n
- Set Nodes' Head

"""

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


if __name__ == "__main__":
    # set nodes
    one = Node(1)
    two = Node(2)
    three = Node(3)

    # connect nodes circular
    one.next_node = two
    two.next_node = three
    three.next_node = one

    # set head
    circular_linked_list = CircularLinkedList()
    circular_linked_list.head = one
