class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = 0
        hsh = {}
        for str in words:
            val = 0
            for char in str:
                val = val | 1<<(ord(char) - ord("a"))
            hsh[str] = val

        for i in xrange(0, len(words)):
            for j in xrange(i + 1, len(words)):
                if len(words[i]) * len(words[j]) > result and hsh[words[i]] & hsh[words[j]] == 0:
                    result = max(result, len(words[i] * len(words[j])))

        return result


obj = Solution()
obj.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])