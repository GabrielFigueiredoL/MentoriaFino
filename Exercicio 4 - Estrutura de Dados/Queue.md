A queue is a linear data structure that follows the `First In, First Out FIFO ` principle, meaning that the first element added to the queue is the first one to be removed.
![[QueueImage.png]]
## Python
```python
queue = []
# Enqueue
queue.append('A')
# Dequeue
element = queue.pop(0)
# Peek
frontElement = queue[0]
# isEmpty
isEmpty = not bool(queue)
# Size
len(queue)

# OR

from collections import deque
queue = deque()
```

## Java
```java
import java.util.LinkedList;
import java.util.Queue;
Queue<Integer> queue = new LinkedList<>();
```