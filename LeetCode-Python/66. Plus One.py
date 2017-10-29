class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1

        for i in xrange(len(digits) - 1, -1, -1):
            sum = digits[i]
            sum = sum + carry
            carry = sum / 10
            sum = sum % 10
            digits[i] = sum

        if carry > 0:
            digits.insert(0, carry)

        return digits