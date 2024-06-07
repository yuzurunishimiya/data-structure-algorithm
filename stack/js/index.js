function createStack() {
    return new Array();
}

function checkEmpty(stack) {
    return stack.length == 0;
}

function push(stack, item) {
    stack.push(item);
}

function pop(stack) {
    if (checkEmpty(stack)) {
        return "stack is empty";
    }
    return stack.pop();
}

const newStack = createStack()
push(newStack, "1");
push(newStack, "2");
push(newStack, "3");
push(newStack, "4");
console.log("popped item: ", pop(newStack))
console.log("stack after popping an element: ", newStack)
