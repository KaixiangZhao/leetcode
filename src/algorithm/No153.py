class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[-1]
        mid = len(nums) // 2
        if nums[0] < nums[mid]:
            if nums[-1] >= nums[mid]:
                return self.findMin(nums[:mid])
            else:
                return self.findMin(nums[mid + 1:])
        else:
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            else:
                return self.findMin(nums[:mid])

if __name__ == "__main__":
    print(Solution().findMin([1,2]))