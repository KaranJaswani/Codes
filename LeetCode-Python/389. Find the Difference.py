class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for char in s:
            res = res ^ ord(char)

        for char in t:
            res = res ^ ord(char)

        return chr(res)



obj = Solution()
obj.findTheDifference("abcd", "acdbe")