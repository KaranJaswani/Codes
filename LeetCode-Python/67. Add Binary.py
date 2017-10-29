class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = '0'
        result = ""
        length = max(len(a), len(b))
        a = a.rjust(length, '0')
        b = b.rjust(length, '0')

        for i in range(length - 1, -1, -1):
            charA = a[i]
            charB = b[i]
            if charA == charB:
                result = carry + result
                carry = charA
            else:
                if carry == '0':
                    result = '1' + result
                else:
                    result = '0' + result

        if carry == '1':
            result = '1' + result

        return result

obj = Solution()
obj.addBinary("011", "01")