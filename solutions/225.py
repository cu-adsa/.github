from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.size = 0
        
    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1
        for _ in range(self.size - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        self.size -= 1
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return not self.size
