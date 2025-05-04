Linked List that each node has two pointers, one pointing to the next node and one pointing to the previous node. This allows for quick and easy insertion and deletion of nodes from the list, as well as efficient traversal of the list in both directions. 
![[DoublyLinkedListImage.png]]
## When to use
- Need to traverse in both directions;
- Remove or insert when already have a reference to the node;
- Dynamic memory allocation.

## Java
### Native
```java
import java.util.LinkedList;
LinkedList<Integer> linkedlist = new LinkedList<>();
```

### Custom
```java
class Node {
    int data;
    Node prev, next;
    Node(int data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

class DoublyLinkedList {
    Node head;
    public void insertEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
        newNode.prev = temp;
    }
}
```

## Python
### Native
```python
from collections import deque
linkedlist = deque()
```

### Custom
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
```
