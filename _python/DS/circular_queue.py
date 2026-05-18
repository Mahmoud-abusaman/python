class MyCircularQueue:

    def __init__(self, k: int):
        self.start = -1
        self.end = -1
        self.capacity = k
        self.size = 0
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.start = self.end = 0
            self.queue[self.end] = value
        else:
            self.end = ((self.end + 1) % self.capacity)
            self.queue[self.end] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = ((self.start + 1) % self.capacity)
        self.size -= 1
        if self.isEmpty():
            self.start = self.end = -1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1  
        else :
            return self.queue[self.start]

    def Rear(self) -> int:
        if self.size == 0:
            return -1  
        else :
            return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity



