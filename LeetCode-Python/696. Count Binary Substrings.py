class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        splitStrings = []
        start = 0
        i = 0
        while i < len(s):
            if i == 0 or s[i] == s[i - 1]:
                i += 1
            elif s[i] != s[i - 1]:
                splitStrings.append(len(s[start:i]))
                start = i
                i += 1

        splitStrings.append(len(s[start:]))

        res = 0
        for i in range(1, len(splitStrings)):
            res += min(splitStrings[i], splitStrings[i - 1])
        
        return res

obj = Solution()
obj.countBinarySubstrings("00110011")
