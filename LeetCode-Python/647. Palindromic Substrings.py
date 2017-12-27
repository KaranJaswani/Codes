class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        while i < len(s):
            res += self.checkOdd(s, i) + self.checkEven(s, i)
            i += 1
        
        return res
    
    def checkOdd(self, s, i):
        res = 1
        x = 1
        while (i - x) >= 0 and (i + x) < len(s):
            if s[i - x] == s[i + x]:
                res += 1
                x += 1
            else:
                break
        
        return res
            
    def checkEven(self, s, i):
        res = 0
        x = 1
        while i >= 0 and (i + x) < len(s):
            if s[i] == s[i + x]:
                res += 1
                x += 2
                i -= 1
            else:
                break
        
        return res
            
o = Solution()
o.countSubstrings('aaa')