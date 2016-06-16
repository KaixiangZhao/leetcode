class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.minn = [2 ** 32 - 1]
        self.list = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.list.append(x)
        self.minn.append(min(self.minn[-1], x))


    def pop(self):
        """
        :rtype: void
        """
        self.list.pop()
        self.minn.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minn[-1]
