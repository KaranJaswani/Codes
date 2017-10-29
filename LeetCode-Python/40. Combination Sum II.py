class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        lst = []
        candidates.sort()
        self.backtrackCombinationSum2(candidates, target, lst, result, -1)
        return result


    def backtrackCombinationSum2(self, candidates, target, lst, result, i):
        if target < 0:
            return

        if target == 0:
            if not result.__contains__(lst):
                result.append(list(lst))
            return

        for j in xrange(i + 1, len(candidates)):
            lst.append(candidates[j])
            self.backtrackCombinationSum2(candidates, target - candidates[j], lst, result, j)
            lst.pop()


obj = Solution()
obj.combinationSum2([10,1,2,7,6,1,5], 8)
