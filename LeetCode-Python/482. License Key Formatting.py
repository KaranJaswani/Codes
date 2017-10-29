class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        lst = list(S.replace('-', '').upper())
        res = ""
        lst = lst[::-1]
        count = 0
        for char in lst:
            if count == K:
                res = '-' + res
                count = 0
            res = char + res
            count += 1

        return res

obj = Solution()
obj.licenseKeyFormatting("2-4A0r7-4k", 4)