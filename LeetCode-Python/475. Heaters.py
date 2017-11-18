class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        houses.sort()
        i = r = 0
        
        for house in houses:
            while house >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - house))
            
        return r
        
o = Solution()
o.findRadius([1,2,3],
[2])