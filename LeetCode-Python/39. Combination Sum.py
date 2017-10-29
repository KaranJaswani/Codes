class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        lst = []
        self.backtrackCombinationSum(candidates, target, lst, result, 0)
        return result


    def backtrackCombinationSum(self, candidates, target, lst, result, i):
        if target < 0:
            return

        if target == 0:
            result.append(list(lst))
            return

        for j in xrange(i, len(candidates)):
            lst.append(candidates[j])
            self.backtrackCombinationSum(candidates, target - candidates[j], lst, result, j)
            lst.pop()


obj = Solution()
obj.combinationSum([2,3,6,7], 7)