class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1]
        for i in range(3, n + 1):
            dp.append(0)
            for j in range(i):
                dp[i] = max(dp[i], max(dp[i - j], i - j) * max(dp[j], j))
        return dp[n]
