# Queue vs Deque (Python)

## Queue (FIFO)

A **queue** is **first-in-first-out (FIFO)**:

- **Enqueue:** Add elements at the back.
- **Dequeue:** Remove elements from the front.

```python
from queue import Queue

q = Queue()
q.put(1)   # enqueue
q.put(2)
q.put(3)

print(q.get())  # 1
print(q.get())  # 2
```
- Only allows operations at front and back.
- Thread-safe by default.

## Deque (Double Ended Queue)
A **deque** can add/remove elements from both ends efficiently:
```python
from collections import deque

dq = deque()
dq.append(1)       # add to right (back)
dq.append(2)
dq.appendleft(0)   # add to left (front)

print(dq)          # deque([0, 1, 2])
print(dq.pop())    # remove from right -> 2
print(dq.popleft())# remove from left  -> 0
print(dq)          # deque([1])
```
- Can be used as stack, queue, or deque.
- Not thread-safe by default.