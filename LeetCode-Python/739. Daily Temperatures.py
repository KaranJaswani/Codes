class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] <= temperatures[i]:
                stack.pop(-1)
            
            if len(stack) == 0: 
                res[i] = 0
            else:
                res[i] = stack[-1][1] - i
            
            stack.append((temperatures[i], i))
        
        return res

obj = Solution()
obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])            