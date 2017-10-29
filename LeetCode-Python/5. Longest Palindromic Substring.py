class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s[0]
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    str = s[i:j + 1]
                    if str == str[::-1]:
                        if len(str) > len(result):
                            result = str

        return result



obj = Solution()
obj.longestPalindrome("c")
# Check the method when we move in opposite directions, i.e each element is considered to the middle of the palindrome





