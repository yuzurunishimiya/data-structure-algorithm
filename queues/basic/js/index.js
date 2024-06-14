class Queue {
    constructor(maxSize) {
        this.queue = new Array(maxSize);
        this.maxSize = maxSize;
        this.head = this.tail = -1;
    }

    enqueue(item) {
        if (this.tail === -1) {
            this.head = 0;
            this.tail = 0;
            this.queue[this.tail] = item;
        } else if ((this.tail + 1) % this.maxSize === 0) {
            console.log("queue if full!")
        } else {
            this.tail += 1;
            this.queue[this.tail] = item;
        }
    }

    dequeue() {
        if (this.head == -1) {
            console.log("Queue is empty!");
            return
        }

        let indexTarget = this.head;
        if ((this.head + 1) % this.maxSize == 0) {
            this.head = -1;
            this.tail = -1;
        } else {
            indexTarget
            this.head += 1;
        }

        let popped = this.queue[indexTarget]
        this.queue[indexTarget] = undefined
        return popped
    }

    getQueue() {
        return this.queue;
    }
}


class Testing {
    constructor(obj) {
        this.obj = obj;
        this.inc = 23;
    }

    insert(length) {
        for (let i=1; i <= length; i++) {
            this.inc += i;
            console.log("--- insert ---")
            console.log("trying to insert: ", this.inc);
            this.obj.enqueue(this.inc);
            console.log("queue-list: ", this.obj.getQueue());
        }
    }

    pop(length) {
        for (let i=1; i <= length; i++) {
            console.log("--- insert ---")
            console.log("popped item: ", this.obj.dequeue());
            console.log("queue-list: ", this.obj.getQueue());
        }
    }
}


const regularQueue = new Queue(6);
console.log(regularQueue.getQueue())
const testingQueue = new Testing(regularQueue)
testingQueue.insert(8);
testingQueue.pop(4);
testingQueue.insert(2);
testingQueue.pop(5);
testingQueue.insert(3);
testingQueue.pop(2);
testingQueue.insert(1);
