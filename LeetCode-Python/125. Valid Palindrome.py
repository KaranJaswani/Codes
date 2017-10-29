class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = list(s)

        i = 0
        j = 0
        while j < len(lst):
            if lst[j].isalpha():
                lst[i] = lst[j].lower()
                i += 1
            j += 1

        lst = lst[0:i]

        return lst == lst[::-1]


obj = Solution()
obj.isPalindrome("0P")