#  Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
from collections import deque

class MyStack:
 
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
    
    def pop(self) -> int:
        
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0