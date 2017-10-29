class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        hashAB = {}
        hashCD = {}

        result = 0
        for i in A:
            for j in B:
                sum = i + j
                if sum in hashAB:
                    hashAB[sum] += 1
                else:
                    hashAB[sum] = 1

        for i in C:
            for j in D:
                sum = i + j
                if sum in hashCD:
                    hashCD[sum] += 1
                else:
                    hashCD[sum] = 1

        for i in hashAB.keys():
            for j in hashCD.keys():
                if i + j == 0:
                    result *= hashAB[i]*hashCD[j]

        return result
