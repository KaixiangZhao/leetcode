class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total=(C - A) * (D - B) + (G - E) * (H - F)
        if E > C or F > D or G < A or H < B:
            return total
        I, J = max(A, E), max(B, F)
        K, L = min(C, G), min(D, H)
        return total - (K - I) * (L - J)
