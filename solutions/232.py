class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        self.transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        self.transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not(self.stack1 or self.stack2)
