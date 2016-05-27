class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        a, b = list(nums1), list(nums2)
        n, m= len(a), len(b)
        if n > m:
            for i in b:
                if i in a:
                    intersection += [i]
                    a.remove(i)
        else:
            for i in a:
                if i in b:
                    intersection += [i]
                    b.remove(i)
        return intersection
