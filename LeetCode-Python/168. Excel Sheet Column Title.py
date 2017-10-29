class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n != 0:
            num = (n - 1) % 26
            n = (n - 1) / 26
            result = chr(65 + num) + result

        return result