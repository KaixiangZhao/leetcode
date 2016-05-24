class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dim = n
        sequence = [dim]
        dim -= 1
        while dim > 0:
            sequence.append(dim)
            sequence.append(dim)
            dim -= 1
        Matrix = [([0] * n) for _ in range(0, n)]
        x = 0
        y = -1
        current = 0
        for i in range(0, len(sequence)):
            if i % 4 == 0:
                for e in range(0, sequence[i]):
                    current += 1
                    y += 1
                    Matrix[x][y] = current
            if i % 4 == 1:
                for e in range(0, sequence[i]):
                    current += 1
                    x += 1
                    Matrix[x][y] = current
            if i % 4 == 2:
                for e in range(0, sequence[i]):
                    current += 1
                    y -= 1
                    Matrix[x][y] = current
            if i % 4 == 3:
                for e in range(0, sequence[i]):
                    current += 1
                    x -= 1
                    Matrix[x][y] = current
        return Matrix
