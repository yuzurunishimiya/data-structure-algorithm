from typing import Any


class Node:
    def __init__(self, item) -> None:
        self.__item = item
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value: Any):
        self.__next = value

    @property
    def item(self):
        return self.__item

class LinkedList:
    def __init__(self) -> None:
        self.__head = None

    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, value: Node):
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
    while next_nodes != None:
        print(next_nodes.item, end=" ")
        next_nodes = next_nodes.next
