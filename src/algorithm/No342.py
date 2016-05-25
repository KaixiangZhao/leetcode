class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask = sum([4**i for i in range(0,16)])
        is_power_of_two = not (num & num - 1)
        is_power_of_four = num & mask == num
        return num > 0 and is_power_of_two and is_power_of_four
