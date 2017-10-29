class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        inc = 0
        result = 0
        for value in hash.values():
            if value == 1:
                inc = 1
            else:
                if value % 2 == 0:
                    result += value
                else:
                    if inc == 0:
                        inc = 1
                    result += value - 1


        return result + inc
