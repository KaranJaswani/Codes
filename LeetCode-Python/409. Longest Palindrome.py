class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        lst = [False] * 128
        for c in s:
            lst[ord(c)] = not lst[ord(c)]
            if not lst[ord(c)]: 
                res += 2
        if res < len(s): 
            res += 1
        
        return res
        
        