class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash1 = {}
        hash2 = {}

        for i in s:
            if not i in hash1.keys():
                hash1[i] = 1
            else:
                hash1[i] += 1

        for i in t:
            if not i in hash2.keys():
                hash2[i] = 1
            else:
                hash2[i] += 1

        return hash1 == hash2


