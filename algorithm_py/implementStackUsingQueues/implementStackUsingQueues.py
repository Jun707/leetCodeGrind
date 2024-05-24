class MyStack:

    def __init__(self):
        self.arr = deque()
        
    def push(self, x: int) -> None:
        self.arr.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.arr)-1):
            self.arr.append(self.arr.popleft())
        return self.arr.popleft()
        
    def top(self) -> int:
        return self.arr[-1]

    def empty(self) -> bool:
        return len(self.arr)==0