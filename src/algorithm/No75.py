class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, k, n = -1, -1, len(nums)
        for j in range(n):
            if nums[j] <= 1:
                k += 1
                nums[k], nums[j] = nums[j], nums[k]
                if nums[k] == 0:
                    i += 1
                    nums[k], nums[i] = nums[i], nums[k]


if __name__ == "__main__":
    nums = [0,2,1,2,1,0,1,2,1,0]
    Solution().sortColors(nums)
    print(nums)