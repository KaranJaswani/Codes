class Solution(object):
    hash = {2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        res = []
        self.backtrackLetterCombinations(0, digits,"", res)
        return res

    def backtrackLetterCombinations(self, k, digits, str, result):
        if len(str) == len(digits):
            result.append(str)
            return

        for i in range(k, len(digits)):
            for j in self.hash[int(digits[i])]:
                self.backtrackLetterCombinations(i + 1, digits, str + j, result)
