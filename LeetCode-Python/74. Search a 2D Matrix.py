class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        checkList = None
        for lst in matrix:
            if len(lst) > 0 and target <= lst[-1]:
                checkList = lst
                break

        if checkList != None:
            for i in range(len(checkList) - 1, -1, -1):
                if target == checkList[i]:
                    return True

        return False