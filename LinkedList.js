const Node = require('./Node');
class LinkedList {
    constructor() {
        this.head = null;
    }
    addFirst(node) {
        node.next = this.head
        this.head = node
    }
    addLast(node) {
        if (!this.head) {
            this.addFirst(node)
            return
        }
        let curr = this.head
        while (curr.next) {
            curr = curr.next
        }
        curr.next = node
    }
    indexOf(node) {
        let curr = this.head
        let index = 0
        while (curr !== node && curr.next !== null) {
            curr = curr.next
            index += 1
        }
        return index;
    }
    removeAt(index) {
        let i = 0;
        let curr = this.head
        let previous = this.head 
        if (index === 0) {
            this.head = this.head.next
        } else if (curr.next === null) {
            previous.next = null
        } else {
            while (i !== index + 1) {
                if (i === index - 1) {
                    previous = curr
                } else if (i === index) {
                    previous.next = curr.next
                }
                i++
                curr = curr.next
            }
        }
    }
}

const list = new LinkedList();
const node1 = new Node(1);
const node2 = new Node(2);
const node3 = new Node(3);
const node4 = new Node(4);
list.addFirst(node1);
list.addFirst(node2);
list.addFirst(node3);
list.addFirst(node4);
list.removeAt(2);
const index1 = list.indexOf(node1)
const index2 = list.indexOf(node2)
const index3 = list.indexOf(node3)
const index4 = list.indexOf(node4)
module.exports = LinkedList;