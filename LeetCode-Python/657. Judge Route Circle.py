class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical = 0
        horizontal = 0
        for move in moves:
            if move is 'U':
                vertical += 1
            elif move is 'D':
                vertical -= 1
            elif move is 'R':
                horizontal += 1
            elif move is 'L':
                horizontal -= 1
        
        return vertical == 0 and horizontal == 0

o = Solution()
print(o.judgeCircle("LL"))
        