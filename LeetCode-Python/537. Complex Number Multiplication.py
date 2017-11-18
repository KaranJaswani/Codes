class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1 = a.split('+')
        l2 = b.split('+')
        r1 = int(l1[0]) if l1[0][0] != '-' else (-1 * int(l1[0][1:]))
        r2 = int(l2[0]) if l2[0][0] != '-' else (-1 * int(l2[0][1:]))
        i1 = int(l1[1][:len(l1[1]) - 1]) if l1[1][0] != '-' else (-1 * int(l1[1][1:len(l1[1]) - 1]))
        i2 = int(l2[1][:len(l2[1]) - 1]) if l2[1][0] != '-' else (-1 * int(l2[1][1:len(l2[1]) - 1]))
        r = (r1*r2) - (i1*i2)
        i = (r1*i2) + (r2*i1)
        return str(r) + "+" + str(i) + "i"

o = Solution()
print(o.complexNumberMultiply("1+-1i", "1+-1i"))