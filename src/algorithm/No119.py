class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        list = [1, 1]
        for i in range(1, rowIndex):
            list.insert(1, list[0] + list[1])
            for j in range(1, i):
                list.insert(j + 2, list[j + 1] + list[j + 2])
                del(list[j + 1])
        return list
