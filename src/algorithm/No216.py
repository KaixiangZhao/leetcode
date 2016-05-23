class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        self.fun(output, [], k, n)
        return output

    def fun(self, output, list, k, n):
        if k == 0:
            output.append(list)
            return
        if k == 1:
            if n < 10:
                output.append(list + [n])
            return
        if len(list) == 0:
            for i in range(1, int((n - 1) / k) + 1):
                if i < 10:
                    self.fun(output, list + [i], k - 1, n - i)
            return
        for i in range(list[-1] + 1, int((n - 1) / k) + 1):
            if i < 10:
                self.fun(output, list + [i], k - 1, n - i)


if __name__ == "__main__":
    print(Solution().combinationSum3(2,18))