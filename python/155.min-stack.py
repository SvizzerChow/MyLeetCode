class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.insert = []
        self.min = []
        self.size = 0


    def push(self, x: int) -> None:
        self.insert.append(x)
        if len(self.min) > 0:
            if self.min[self.size-1] > x:
                self.min.append(x)
            else:
                self.min.append(self.min[self.size-1])
        else:
            self.min.append(x)
        self.size += 1


    def pop(self) -> None:
        x = self.insert.pop()
        self.min.pop()
        self.size -= 1
        return x

    def top(self) -> int:
        return self.insert[self.size-1]

    def getMin(self) -> int:
        return self.min[self.size-1]


s = MinStack()

s.push(-2)
s.push(0)
s.push(-1)

print(s.ordered)
print(s.insert)

print(s.getMin())
print()