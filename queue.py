class MyQueue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        self.index += 1
        return self.queue[self.index-1]

    def peek(self) -> int:
        return self.queue[self.index] 

    def empty(self) -> bool:
        if self.index == len(self.queue):
            return True
        else:
            return False
    
    def __str__(self):
        if str.queue[self.index:]:
            return str(self.queue[self.index:])
        else:
            return 
