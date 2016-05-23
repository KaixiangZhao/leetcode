class Solution(object):

    def __init__(self):
        self.count=0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.DFS(n, [], [], [])
        return self.count

    def DFS(self, n, queens, xy_diff, xy_sum):
        p = len(queens)
        if p == n:
            self.count += 1
            return
        for q in range(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                self.DFS(n, queens + [q], xy_diff + [p - q], xy_sum + [p + q])