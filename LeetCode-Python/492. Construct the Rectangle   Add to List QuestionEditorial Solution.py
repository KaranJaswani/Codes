import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        num = int(math.sqrt(area))

        while area % num != 0:
            num += 1

        return [max(num, area/num), min(num, area/num)]


