class MyQueue:

    def __init__(self):
        self.first_stack: List[int] = []
        self.second_stack: List[int] = []

    def push(self, x: int) -> None:
        self.first_stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            while not len(self.first_stack) == 1:
                self.second_stack.append(self.first_stack.pop())
            element: int = self.first_stack.pop()
            while not len(self.second_stack) == 0:
                self.first_stack.append(self.second_stack.pop())
            return element
            
    def peek(self) -> int:
        if not self.empty():
            while not len(self.first_stack) == 1:
                self.second_stack.append(self.first_stack.pop())
            element: int = self.first_stack[0]
            self.second_stack.append(self.first_stack.pop())
            while not len(self.second_stack) == 0:
                self.first_stack.append(self.second_stack.pop())
            return element        

    def empty(self) -> bool:
        return len(self.first_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
