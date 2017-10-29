class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = {}
        for char in s:
            if char in lst.keys():
                lst[char] += 1
            else:
                lst[char] = 1

        lst = sorted(lst.items() , key=lambda (h, k): (-k, h))
        result = ""
        for l in lst:
            result += l[0]*l[1]

        return result