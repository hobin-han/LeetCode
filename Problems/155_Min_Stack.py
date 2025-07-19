# https://leetcode.com/problems/min-stack

class MinStack(object):

    def __init__(self):
        self.main = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.main) == 0:
            self.min.append(val)
        else:
            last_min = self.min[-1]
            if val < last_min:
                self.min.append(val)
            else:
                self.min.append(last_min)
        self.main.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        self.main.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.main) == 0:
            return None

        return self.main[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min) == 0:
            return None

        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
