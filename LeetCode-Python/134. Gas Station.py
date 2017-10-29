class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        spare = []
        for i in range(0, len(gas)):
            spare.append(gas[i] - cost[i])

        if len(spare) == 1:
            if spare[0] < 0:
                return -1
            else:
                return 0

        i = 0
        j = 0
        count = 0
        visited = 0

        while count != len(gas) and visited < len(gas):
            j = i
            totalSpare = spare[j]
            while totalSpare >= 0 and count < len(gas):
                j = j + 1
                totalSpare += spare[j%len(gas)]
                count += 1

            if count == len(gas):
                return i
            else:
                if i == j:
                    j = j + 1
                visited += j - i
                i = j
                count = 0

        return -1


obj = Solution()
obj.canCompleteCircuit([1,2], [2,1])


