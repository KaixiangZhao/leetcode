class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        min_sum = [[0] * n for _ in range(m)]
        min_sum[0][0] = grid[0][0]
        for i in range(1, m):
            min_sum[i][0] = min_sum[i - 1][0] + grid[i][0]
        for j in range(1, n):
            min_sum[0][j] = min_sum[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                min_sum[i][j] = grid[i][j] + min(min_sum[i - 1][j], min_sum[i][j - 1])
        return min_sum[m - 1][n - 1]
