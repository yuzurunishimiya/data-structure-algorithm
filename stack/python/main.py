""" Stack """
# Linear Data Structure that follows the principle LIFO
# LIFO -> Last In First Out

# YOU CAN DO:
# -> Put a new plate on top -> remove the top plate

# Principle:
# -> Empty Stack
# > Push to stack
# -> Push another one (dst sampai full/sepertlunya)
# -> pop (mengeluarkan dari stack)

# Push: Add an element to stack
# Pop: Remove an element from stack
# IsEmpty: Check if stack is empty
# IsFull: Check if stack is full
# Peek: Get the value of the top element without removing it


from typing import Any, List


# Stack implementation in python
# from programiz


# Creating a stack

def create_stack():
    stack = []
    return stack


# Creating an empty stack

def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


# Creating by myself


class Stack:
    """Stack's class"""

    def __init__(self) -> None:
        self.__stack: List[Any] = []

    def check_empty(self) -> bool:
        """check if stack is empty"""
        return len(self.__stack) == 0

    def push(self, item) -> None:
        """insert item into stack"""
        self.__stack.append(item)
        print("pushed item: " + item)

    def pop(self) -> Any:
        """remove from stack"""
        if self.check_empty():
            return "stack is empty"
        return self.__stack.pop()

    def get_stack(self) -> List[Any]:
        """get stack"""

        return self.__stack


new_stack = Stack()
for i in range(1, 5):
    new_stack.push(item=str(i))

print("popped item: " + stack.pop())
print("stack after popping an element: " + str(new_stack.get_stack()))
