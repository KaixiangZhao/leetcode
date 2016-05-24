class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        res = [1]
        for i in range(1, len(nums)):
            max_length = 1
            for j in range(0,i):
                if nums[j] < nums[i]:
                    max_length = max(max_length, res[j]+1)
            res.append(max_length)
        return max(res)
