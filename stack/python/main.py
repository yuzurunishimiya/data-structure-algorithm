from typing import Any, Literal


class Stack:
    def __init__(self) -> None:
        self.__stack: list = []

    @property
    def stack(self):
        return self.__stack

    def check_empty(self) -> bool:
        if len(self.__stack) == 0:
            return True
        return False

    def add_item(self, item: Any) -> None:
        self.__stack.append(item)
        print("pushed item", item)

    def pop_item(self) -> Any:
        if self.check_empty():
            return "Stack empty"
        return self.__stack.pop()



if __name__ == "__main__":
    stack = Stack()
    stack.add_item(str(1))
    stack.add_item(str(2))
    stack.add_item(str(3))
    print("pop item: ", stack.pop_item())
    print(stack.stack)
    print("pop item: ", stack.pop_item())
    print(stack.stack)
    stack.add_item(str(4))
    print(stack.stack)
    print("pop item: ", stack.pop_item())
    print(stack.stack)
    print("pop item: ", stack.pop_item())
    print(stack.stack)
    print("pop item: ", stack.pop_item())
    print(stack.stack)
