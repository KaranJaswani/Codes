class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        for x in xrange(1, n):
            temp = ""
            i = 0
            while i < len(result):
                count = 0
                j = i
                while j < len(result):
                    if count == 0 or result[j] == result[j - 1]:
                        count += 1
                    else:
                        break
                    j += 1
                temp = temp + ('%d%c' % (count, result[j - 1]))
                i = j
            result = temp

        return result

