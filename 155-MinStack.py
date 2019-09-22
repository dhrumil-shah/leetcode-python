"""
155. Min Stack
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackArray = []
        self.minIndex = 0    

    def push(self, x: int) -> None:        
        self.stackArray.append(x)
        if (x < self.stackArray[self.minIndex]):
            self.minIndex = len(self.stackArray)-1
        

    def pop(self) -> None:        
        oldMin = self.getMin()
        x = self.stackArray.pop()
        if (x <= oldMin and len(self.stackArray) > 0):
            minIndex = self.findMinIndex()
        
    def findMinIndex(self) -> int:
        newMin = self.stackArray[0]
        self.minIndex = 0
        for i in range(1, len(self.stackArray)):
            if (self.stackArray[i] < newMin):
                print("newMin" , newMin)
                self.minIndex = i
                newMin = self.stackArray[i]

    def top(self) -> int:
        if  len(self.stackArray) > 0:
            return self.stackArray[-1]

    def getMin(self) -> int:
        return self.stackArray[self.minIndex]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.push(0)
obj.push(-3)
obj.push(-2)
obj.push(-5)

print(obj.top())
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())