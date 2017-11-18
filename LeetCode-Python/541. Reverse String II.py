class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        i = 0
        while i < len(s):
            substr = s[i:i + 2 * k]
            res = res + substr[:k][::-1] + substr[k:]
            i = i + 2 * k
        
        return res

        