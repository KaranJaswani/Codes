class Solution(object):
    row = 0
    col = -1
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        origR = len(nums)
        origC = len(nums[0]) if origR > 0 else 0

        if (origR*origC) != (r*c):
            return nums

        i = 0
        j = 0
        res = []
        lst = []
        while i < r:
            if j == c:
                i += 1
                j = 0
                res.append(lst)
                lst = []
            
            elem = self.getNextElement(nums, origR, origC)
            
            if elem == None:
                break

            lst.append(elem)
            j += 1
        
        return res
    
    def getNextElement(self, nums, totalRows, totalColumns):
        self.col += 1
        if self.col == totalColumns:
            self.row += 1
            self.col = 0

        if self.row == totalRows:
            return None

        return nums[self.row][self.col]

o = Solution()
o.matrixReshape([[1,2],[3,4]], 1, 4)

