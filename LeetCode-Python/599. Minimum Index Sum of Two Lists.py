import sys

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in range(0, len(list1)):
            dict[list1[i]] = [i]
        
        for i in range(0, len(list2)):
            if list2[i] in dict:
                dict[list2[i]].append(i)
        
        minSum = sys.maxint
        res = []
        for key in dict:
            if len(dict[key]) > 1:
                if minSum > sum(dict[key]):
                    res = [key]
                    minSum = sum(dict[key])
                elif minSum == sum(dict[key]):
                    res.append(key)
        
        return res
                    
obj = Solution()
obj.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])