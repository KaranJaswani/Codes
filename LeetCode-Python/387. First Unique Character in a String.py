class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in xrange(0, len(s)):
            if s.find(s[i], i + 1) == -1 and s.find(s[i], 0, i) == -1:
                return i

        return -1