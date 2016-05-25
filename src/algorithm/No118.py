class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(1, numRows):
            list = [1,1]
            for j in range(i - 1):
                list.insert(j + 1, result[i - 1][j] + result[i - 1][j + 1])
            result.append(list)
        return result
