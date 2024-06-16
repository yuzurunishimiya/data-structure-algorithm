"""
Linked List Doubly:
    adding a ponter or refenrence to previous node in a linked-list;
    direction: forward / backward;

    Head|null <-> [prev|data|next] <-> [prev|data|next] <-> Null
"""

from typing import Any, Optional
from random import choice


class Node:
    """Doubly LL node's class"""

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def next_(self) -> Optional['Node']:
        """get next node"""
        return self.__next

    @next_.setter
    def next_(self, next_node: 'Node') -> None:
        """set next node"""

        if not isinstance(next_node, Node):
            print("invalid value of next_node, Node object expected")
        else:
            self.__next = next_node

    @property
    def prev_(self) -> Optional['Node']:
        """get previous node"""
        return self.__prev

    @prev_.setter
    def prev_(self, previous_node: 'Node') -> None:
        """set previous node"""

        if not isinstance(previous_node, Node):
            print("invalid value of previous, Node object expected")
        else:
            self.__prev = previous_node

    @property
    def data(self) -> Any:
        """get node's data"""

        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        """set value of node's data"""

        self.__data = value


class DoublyLinkedList:
    """Doubly LL's class"""

    def __init__(self, head_node: Optional[Node] = None) -> None:
        self.__head: Optional[Node] = head_node

    @property
    def head(self) -> Optional[Node]:
        """get head's node"""

        return self.__head

    @head.setter
    def head(self, node: Node) -> None:
        """set value of Linked List head"""

        self.__head = node

    def insert_at_beginning(self, new_data: Any) -> None:
        """to insert data to beginning of LL (set as head)"""

        # 1. create new node
        # 2. set head prev (if exists) to new node
        # 3. set current head node as next node to new node
        # 4. set new node as head of LL

        new_node = Node(new_data)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next_ = self.__head
            self.__head = new_node

    def insert_before(self, next_node: Node, new_node_data: Any) -> None:
        """to insert before a node"""

        if not isinstance(next_node, Node):
            print("next node must be a node object")
        elif next_node == self.__head:
            self.insert_at_beginning(new_node_data)
        else:
            new_node = Node(new_node_data)
            new_node.prev_ = next_node.prev_
            new_node.next_ = next_node

            next_node.prev_.next_ = new_node
            next_node.prev_ = new_node

    def insert_after(self, previous_node: Node, new_node_data: Any) -> None:
        """to insert after a node"""

        if not isinstance(previous_node, Node):
            print("next node must be a node object")
        else:
            new_node = Node(new_node_data)
            new_node.next_ = previous_node.next_
            new_node.prev_ = previous_node
            previous_node.next_ = new_node

    def insert_at_end(self, new_node_data: Any) -> None:
        """to insert at the end of LL"""

        new_node = Node(new_node_data)
        if self.__head is None:
            self.__head = new_node
        else:
            last_node = self.__head
            while last_node.next_:
                last_node = last_node.next_

            new_node.prev_ = last_node
            last_node.next_ = new_node

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
            self.__head = temp.next_
            return temp
        else:
            cur = self.__head
            for _ in range(position):
                if cur is None:
                    break

                cur = cur.next_

            if cur is None:
                print("position is higher than linked list length!")
                return

            temp = cur
            cur.prev_.next_ = cur.next_
            cur.next_.prev_ = cur.prev_

            return temp

    def search(self, key: Any) -> Optional[Node]:
        """to search based on data/key"""

        cur = self.__head
        while cur.next_:
            if cur.data == key:
                return cur

            cur = cur.next_

        return None

    def sort(self, reversed_sort: bool = False):
        """not implemented yet"""

    def print_list(self, reverse: bool = False) -> None:
        """print linked-list"""

        if reverse:
            node = self.__head
            while node.next_ is not None:
                node = node.next_

            while node is not None:
                print(f"{node.data} ", end=" ")
                node = node.prev_
        else:
            node = self.__head
            while node is not None:
                print(f"{node.data} ", end=" ")
                node = node.next_

        print() # to the grand line


if __name__ == "__main__":
    numbers = [x for x in range(1,100)]
    arr_pop = [choice(numbers) for _ in range(15)]

    llist = DoublyLinkedList()
    llist.insert_at_beginning(0)

    for item in arr_pop:
        llist.insert_at_end(item)

    print("original: ")
    llist.print_list()
    print("reverse: ")
    llist.print_list(reverse=True)
    llist.insert_after(llist.head, new_node_data=-10)
    llist.print_list()
    knode = llist.search(key=-10)
    llist.insert_before(knode, new_node_data=-20)
    llist.print_list()
    knode = llist.search(key=-100)
    print("node search -100:", knode)
    deleted = llist.delete_node(2)
    print("deleted node: ", deleted.data)
    llist.print_list()
