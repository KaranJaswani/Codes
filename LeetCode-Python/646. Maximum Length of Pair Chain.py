# DP: Time Limit Exceeded
# class Solution(object):
#     def findLongestChain(self, pairs):
#         """
#         :type pairs: List[List[int]]
#         :rtype: int
#         """
#         def helper(pairs, start, last, dp):
#             if start in dp:
#                 return dp[start]

#             res = 0
#             for i in range(start, len(pairs)):
#                 if last == None or last[1] < pairs[i][0]:
#                     res = max(res, 1 + helper(pairs, i + 1, pairs[i], dp))
            
#             dp[start] = res
#             return res
            
#         pairs = sorted(pairs,key=lambda x: (x[0], x[1]))
#         return helper(pairs, 0, None, {})

import sys
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs,key=lambda x: x[1])
        last = [-sys.maxint - 1, -sys.maxint - 1]
        res = 0
        for pair in pairs:
            if pair[0] > last[1]:
                last = pair
                res += 1
        return res
            

obj = Solution()
obj.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
                 
