class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.fun(result, [], nums, len(nums))
        return result

    def fun(self, result, list, nums, n):
        if n == 0:
            result.append(list)
            return
        for i in range(len(nums)):
            self.fun(result, list + [nums[i]], nums[:i]+nums[i+1:], n - 1)


if __name__ == "__main__":
    print(Solution().permute([1,2,3]))
