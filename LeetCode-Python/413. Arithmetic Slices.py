class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Naive Solution
        # if len(A) < 3:
        #     return 0

        # i = 0
        # j = 1
        # diff = A[j] - A[i]
        # result = 0
        # while j + 1 < len(A):
        #     if A[j + 1] - A[j] == diff:
        #         j += 1
        #     else:
        #         if j - i >= 2:
        #             n = j - i - 1
        #             n = (n * (n + 1))/2
        #             result += n
        #         i = j
        #         j = j + 1
        #         diff = A[j] - A[i]

        # if j - i >= 2:
        #     n = j - i - 1
        #     n = (n * (n + 1)) / 2
        #     result += n

        # return result

        # DP Solution
        j = 0
        result = 0
        i = 2
        for i in xrange(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                j += 1
                result += j
            else:
                j = 0

        return result
