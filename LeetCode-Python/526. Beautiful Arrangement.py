# class Solution(object):
#     def countArrangement(self, N):
#         return self.helper(N, tuple(range(1, N + 1)), {})

#     def helper(self, i, X, cache):
#             if i == 1:
#                 return 1

#             key = (i, X)
#             if key in cache:
#                 return cache[key]

#             total = 0
#             for j in xrange(len(X)):
#                 if X[j] % i == 0 or i % X[j] == 0:
#                     total += self.helper(i - 1, X[:j] + X[j + 1:], cache)
                    
#             cache[key] = total
#             return total

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = (N + 1) * [False]
        return self.generatePermutations(1, N, used)
        

    def generatePermutations(self, len, N, used):
        if len > N:
            return 1
        
        localRes = 0
        for i in range(1, N + 1):
            if not used[i] and (i % len == 0 or len % i == 0):
                used[i] = True
                localRes += self.generatePermutations(len + 1, N, used)
                used[i] = False
        
        return localRes
    
o = Solution()
print(o.countArrangement(4))

    