A stack is a linear data structure that follows the follows the `Last In First Out (LIFO)` principle, meaning that the last element added to the stack is the first one to be removed.
There are two types of stack: **fixed size stack** and **dynamic size stack**.
![[stackImage.png]]
## Fixed size Stack
A fixed size stack has a fixed size and cannot grow or shrink dynamically. If the stack is full and an attempt is made to add an element to it, an overflow error occurs; if the stack is empty and an attempt is made to remove an element from it, an overflow error occurs.
## Dynamic size Stack
A dynamic size stack can grow or shrink dynamically. When the stack is full, it automatically increases its size to accommodate the new element, and when the stack is empty, it decreases its size.

## Python
```python
stack = []
# Push
stack.append('A')
# Pop
element = stack.pop()
# Peek
topElement = stack[-1]
# isEmpty
isEmpty = not bool(stack)
# Size
len(stack)
```

## Java
```java
import java.util.Stack;
Stack<Integer> stack = new Stack<>();
```