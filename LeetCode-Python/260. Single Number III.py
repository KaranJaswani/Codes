# Once again, we need to use XOR to solve this problem. But this time, we need to do it in two passes:

# In the first pass, we XOR all elements in the array, and get the XOR of the two numbers we need to find. Note that since the two numbers are distinct, so there must be a set bit (that is, the bit with value '1') in the XOR result. Find
# out an arbitrary set bit (for example, the rightmost set bit).

# In the second pass, we divide all numbers into two groups, one with the aforementioned bit set, another with the aforementinoed bit unset. Two different numbers we need to find must fall into thte two distrinct groups. XOR numbers in each group, we can find a number in either group.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        
        for num in nums:
            xor ^= num
            print xor

        xor &= -xor
        print(xor)
        res = [0, 0]

        for num in nums:   
            if num & xor == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        
        return res


o = Solution()
o.singleNumber([1, 2, 1, 5, 3, 2])