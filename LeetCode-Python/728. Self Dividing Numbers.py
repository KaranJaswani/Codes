class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            tmp = num
            isSelfDividing = True
            while tmp % 10 != 0:
                if num % (tmp % 10) != 0:
                    isSelfDividing = False
                    break
                else:
                    tmp = tmp / 10
                    
            if isSelfDividing and tmp == 0:
                res.append(num)
        
        return res

o = Solution()
print(o.selfDividingNumbers(1, 22))