class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        breakable = []
        for i in range(0, len(s) + 1):
            breakable.append(False)

        breakable[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i + 1):
                if breakable[j] and s[j:i] in wordDict:
                    breakable[i] = True
                    break

        return breakable[len(s)]

    # ******** Iteration is so much better ***********
    #     return self.backtrackWordBreak(s,wordDict,{})
    #
    # def backtrackWordBreak(self,s, wordDict, hash):
    #
    #     if s in hash.keys():
    #         return hash[s]
    #
    #     if s in wordDict:
    #         hash[s] = True
    #         return True
    #
    #     res = False
    #     for i in range(0, len(s) + 1):
    #         if s[0:i] in wordDict:
    #             res = self.backtrackWordBreak(s[i:], wordDict, hash)
    #             hash[s[0:i]] = res
    #             if res: return True
    #         else:
    #             hash[s[0:i]] = False
    #
    #     return False

ob = Solution()
ob.wordBreak("leetcode", ["leet", "code"])
