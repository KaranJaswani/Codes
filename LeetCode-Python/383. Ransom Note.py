class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = {}
        for char in magazine:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for char in ransomNote:
            if char in hash and hash[char] > 0:
                hash[char] -= 1
            else:
                return False

        return True