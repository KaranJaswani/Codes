class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        hsh = {}
        stack = []

        for num in nums:
            while len(stack) > 0 and stack[-1] < num:
                hsh[stack.pop()] = num
            stack.append(num)
            
        res = []
        for num in findNums:
            res.append(hsh.get(num, -1))
        
        return res

o = Solution()
print(o.nextGreaterElement([2, 4], [1,2,3,4]))
        
        