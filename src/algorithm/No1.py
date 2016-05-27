class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if another in map:
                return [map[another], i]
            map[nums[i]] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,14], 18))