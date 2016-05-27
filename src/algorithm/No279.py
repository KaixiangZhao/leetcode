class Solution(object):

    def __init__(self):
        self.least = float('inf')


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dp(n, 0)
        return self.least


    def dp(self, n, k):
        if n < 4:
            k += n
            if k < self.least:
                self.least = k
            return
        k += 1
        if k >= self.least:
            return
        sqrt = int(n ** 0.5)
        if n == sqrt ** 2:
            if k < self.least:
                self.least = k
            return
        for i in range(sqrt, sqrt // 2, -1):
            self.dp(n - i ** 2, k)


if __name__ == "__main__":
    print(Solution().numSquares(1535))