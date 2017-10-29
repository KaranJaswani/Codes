class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in xrange(1, len(str) / 2 + 1):
            if len(str) % i == 0:
                if str[0:i] * (len(str) / i) == str:
                    return True

        return False