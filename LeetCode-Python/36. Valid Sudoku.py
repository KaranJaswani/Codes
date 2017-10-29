class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.checkRows(board) and self.checkColumns(board) and self.checkSquares(board)


    def checkRows(self, board):
        for row in range(0, len(board)):
            if not self.checkRow(board, row):
                return False

        return True

    def checkColumns(self, board):
        for col in range(0, len(board[0])):
            if not self.checkColumn(board, col):
                return False

        return True


    def checkSquares(self, board):
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                if not self.checkSquare(board, i, j):
                    return False

        return True


    def checkRow(self, board, row):
        lst = []
        for num in board[row]:
            if num == "." or num not in lst:
                lst.append(num)
            else:
                return False
        return True

    def checkColumn(self, board, col):
        l = []
        for lst in board:
            if lst[col] == "." or lst[col] not in l:
                l.append(lst[col])
            else:
                return False

        return True

    def checkSquare(self, board, row, col):
        lst = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] == "." or board[i][j] not in lst:
                    lst.append(board[i][j])
                else:
                    return False

        return True

obj = Solution()
obj.isValidSudoku([".87654321",
                   "2........",
                   "3........",
                   "4........",
                   "5........",
                   "6........",
                   "7........",
                   "8........",
                   "9........"])