class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                neighbor = self.get_neighbor(board, i, j)
                if board[i][j] == 1:
                    if neighbor == 2 or neighbor == 3:
                        board[i][j] = 3
                else:
                    if neighbor == 3:
                        board[i][j] = 2
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1


    def get_neighbor(self, board, row, col):
        neighbor = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >=0 and i < len(board) and j >= 0 and j < len(board[0]):
                    neighbor += board[i][j] & 1
        neighbor -= board[row][col] & 1
        return neighbor
