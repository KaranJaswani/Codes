class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        splitstr = str.split(" ")
        hash = {}

        if len(pattern) != len(splitstr):
            return False

        j = 0

        for i in pattern:
            if i in hash.keys():
                if hash[i] != splitstr[j]:
                    return False
            else:
                if not splitstr[j] in hash.values():
                    hash[i] = splitstr[j]
                else:
                    return False


            j += 1

        return True


obj = Solution()
obj.wordPattern("abba", "dog cat cat dog")
