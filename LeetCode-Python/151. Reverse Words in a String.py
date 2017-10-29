class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.strip().split()[::-1])


obj = Solution()
obj.reverseWords("   a    b")
