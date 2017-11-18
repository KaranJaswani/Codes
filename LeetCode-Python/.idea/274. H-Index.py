class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0: return 0
        
        citations.sort()
        l = len(citations)
        for i in range(l - 1, -1, -1):
            if citations[i] == l - i:
                return l - i
        
        return 1

obj = Solution()
obj.hIndex([3, 0, 6, 1, 5])