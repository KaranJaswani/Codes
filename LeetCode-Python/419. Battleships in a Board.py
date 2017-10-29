class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in xrange(0, len(board)):
            for j in xrange(0, len(board[i])):
                if board[i][j] == "X" and \
                    (i - 1 < 0 or board[i - 1][j] == ".") and \
                    (j - 1 < 0 or board[i][j - 1] == "."):
                    result += 1

        return result