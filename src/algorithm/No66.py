class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            digits = [0]
        index = len(digits) - 1
        while True:
            digits[index] += 1
            if digits[index] == 10:
                if index > 0:
                    digits[index] = 0
                    index -= 1
                else:
                    digits[index] = 0
                    digits.insert(index, 1)
                    break
            else:
                break
        return digits
