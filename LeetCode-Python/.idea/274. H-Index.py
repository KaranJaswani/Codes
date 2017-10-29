class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # citations.sort(reverse=True)
        # hIndex = 0
        #
        # for i in range(0, len(citations)):
        #     if citations[i] >= i + 1:
        #         hIndex =  i + 1
        #
        # return hIndex

        tempList = []
        for i in range(0, len(citations) + 1):
            tempList.append(0)

        for i in range(0, len(citations)):
            if citations[i] >= len(citations):
                tempList[-1] += 1
            else:
                tempList[citations[i]] += 1

        sum = 0
        hIndex = 0
        for i in range(len(tempList) - 1, -1, -1):
            tempList[i] = sum + tempList[i]
            sum = tempList[i]
            if sum >= i:
                return i

        return 0

obj = Solution()
obj.hIndex([3, 0, 6, 1, 5])








obj = Solution()
obj.hIndex([2, 0, 6, 1, 5])