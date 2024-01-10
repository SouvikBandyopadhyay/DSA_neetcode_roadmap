class MinStack:

    def __init__(self):
        self.s = list()
        self.minn = list()

    def push(self, val: int) -> None:
        if len(self.minn) == 0 or val <= self.minn[-1]:
            self.minn.append(val)
        self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.minn[-1]:
            self.minn.pop()
        return self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
