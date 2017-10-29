# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.backtrackGenerateParenthesis(n, result, "", 0, 0)
        return result


    def backtrackGenerateParenthesis(self, n, lst, s, i, start):
        if len(s) == 2 * n and i == 0:
            lst.append(str(s))
            return

        if len(s) > 2 * n:
            return

        if len(s) > 0 and i > 0:
            self.backtrackGenerateParenthesis(n, lst, s + ")", i - 1, start)

        for k in xrange(start, n):
            self.backtrackGenerateParenthesis(n, lst, s + "(", i + 1, k + 1)


obj = Solution()
obj.generateParenthesis(3)
