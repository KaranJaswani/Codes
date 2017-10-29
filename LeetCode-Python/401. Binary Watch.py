import math


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        self.backtrackHours(0,0,num,0,-1,result)
        return result

    def backtrackHours(self, hours, minutes, num, setBits, lastBit, result):

        self.backtrackMinutes(hours, minutes, num, setBits, -1, result)
        for i in xrange(lastBit + 1, 4):
            hours += math.pow(2, i)
            setBits += 1
            self.backtrackHours(hours, minutes, num, setBits, i, result)
            hours -= math.pow(2, i)
            setBits -= 1

    def backtrackMinutes(self, hours, minutes, num, setBits, lastBit, result):
        if setBits > num:
            return

        if setBits == num:
            if hours < 12 and minutes < 60:
                if minutes < 10:
                    result.append(str(int(hours)) + ":" + "0" + str(int(minutes)))
                else:
                    result.append(str(int(hours)) + ":" + str(int(minutes)))
            return

        for i in xrange(lastBit + 1, 6):
            minutes += math.pow(2, i)
            setBits += 1
            self.backtrackMinutes(hours, minutes, num, setBits, i, result)
            minutes -= math.pow(2, i)
            setBits -= 1