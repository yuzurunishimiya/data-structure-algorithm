from typing import Any


class Deque:
    def __init__(self) -> None:
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_rear(self, item: Any):
        self.__items.append(item)

    def add_front(self, item: Any):
        self.__items.insert(0, item)

    def remove_front(self):
        if len(self.__items) > 0:
            return self.__items.pop(0)
        return None

    def remove_rear(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        return None

    def size(self):
        return len(self.__items)


if __name__ == '__main__':

    d = Deque()
    d.add_rear(1)
    d.add_rear(2)
    d.add_front(0)
    d.add_front(-1)

    print(d.size())
    print(d.is_empty())
