class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = str((numerator * 1.0) / (denominator * 1.0))
        lst = result.split('.')
        if lst[1] == "0":
            return lst[0]

        for i in range(0, len(lst[1])):
            if lst[1][i] in lst[1][0:i]:
                k = lst[1][0:i].find(lst[1][i])
                temp = lst[1][0:k] + "(" + lst[1][k:i] + ")"
                lst[1] = temp
                break

        return ".".join(lst)



obj = Solution()
obj.fractionToDecimal(1,333)


