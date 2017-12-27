# if you have n number, the maximum k can be n - 1;
# if n is 9, max k is 8.
# This can be done by picking numbers interleavingly from head and tail,

# // start from i = 1, j = n;
# // i++, j--, i++, j--, i++, j--

# 1   2   3   4   5
#   9   8   7   6
# out: 1 9 2 8 3 7 6 4 5
# dif:  8 7 6 5 4 3 2 1
# Above is a case where k is exactly n - 1
# When k is less than that, simply lay out the rest (i, j) in incremental
# order(all diff is 1). Say if k is 5:

#      i++ j-- i++ j--  i++ i++ i++ ...
# out: 1   9   2   8    3   4   5   6   7
# dif:   8   7   6   5    1   1   1   1 

class Solution(object):
    def constructArray(self, n, k):
        res = []
        i = 1
        j = n
        while i <= j:
            if k > 1:
                if k % 2 == 0:
                    res.append(j)
                    j -= 1
                else:
                    res.append(i)
                    i += 1
                k -= 1
            else:
                res.append(i)
                i += 1
        
        return res

obj=Solution()
obj.constructArray(3,2)
