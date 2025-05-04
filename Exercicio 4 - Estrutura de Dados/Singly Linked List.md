Basic Linked list, consists of a node that has 1 data and 1 pointer. The pointer points to the next node and so on. The last node points to null.
![[singlyLinkedListImage.png]]
## When to use
- Only need to traverse the list in one direction;
- When frequent insertions/deletions on the beginning of the list;
- Dynamic memory allocation.
## Java
```java
class Node {
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    Node head;
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    public void delete(int data) {
        if (head == null) return;
        if (head.data == data) {
            head = head.next;
            return;
        }
        Node current = head;
        while (current.next != null && current.next.data != data) {
            current = current.next;
        }
        if (current.next != null) {
            current.next = current.next.next;
        }
    }
}
```

## Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def delete(self, data):
        current = self.head
        if current is not None and current.data == data:
            self.head = current.next
            return
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

```