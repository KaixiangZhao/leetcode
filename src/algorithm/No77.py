class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.recur(res, 0, n + 1, k, [])
        return res

    def recur(self, res, i, n, k, tmp):
        if k == 0:
            res.append(tmp)
            return
        for j in range(i + 1, n):
            self.recur(res, j, n, k - 1, tmp + [j])
