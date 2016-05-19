class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        n = len(sl)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, n-1

        while i < j:
            if sl[i] in vowels and sl[j] in vowels:
                sl[i], sl[j] = sl[j], sl[i]
                i, j = i + 1, j - 1
            elif sl[i] in vowels:
                j = j - 1
            elif sl[j] in vowels:
                i = i + 1
            else:
                i, j = i + 1, j - 1

        return ''.join(sl)