class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        print self.backtrackLongestSubstring(s, k)

    def backtrackLongestSubstring(self, s, k):
        if len(s) < k:
            return 0

        hash = {}
        for char in s:
            if char in hash.keys():
                hash[char] += 1
            else:
                hash[char] = 1

        isBacktrackNeeded = False
        midKey = ''
        for (key,value) in hash.items():
            if value < k:
                isBacktrackNeeded = True
                midKey = key
                break

        if not isBacktrackNeeded:
            return len(s)
        else:
            pos = s.index(midKey)
            left = self.backtrackLongestSubstring(s[0:pos], k)
            right = self.backtrackLongestSubstring(s[pos + 1:], k)

            return max(left, right)


