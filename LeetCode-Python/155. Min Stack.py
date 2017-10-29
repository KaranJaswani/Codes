class MinStack(object):

    stack = []
    minStack = []
    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x > self.stack[0]:
            self.minStack.append(x)
        else:
            while len(self.stack) > 0 and x <= self.stack[-1]:
                self.stack.pop(-1)
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            element = self.stack.pop(-1)
            if element == self.minStack[-1]:
                self.minStack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()