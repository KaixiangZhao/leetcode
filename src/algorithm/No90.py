class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dps(result, [], nums)
        return result


    def dps(self, result, list, nums):
        if len(nums) == 0:
            list.sort()
            if list not in result:
                result.append(list)
            return
        self.dps(result, list + [nums[0]], nums[1:])
        self.dps(result, list, nums[1:])
