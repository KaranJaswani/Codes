class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or (word.islower()) or (word[1:].isLower() and word[0:1].isUpper())
        