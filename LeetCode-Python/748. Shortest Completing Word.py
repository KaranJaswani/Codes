class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def count(word):
            res = [0] * 26
            for letter in word:
                res[ord(letter) - ord('a')] += 1
            return res

        def dominates(w1, w2):
            return all(x1 >= x2 for x1, x2 in zip(w1, w2))

        res = None
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if ((res is None or len(word) < len(res)) and dominates(count(word), target)):
                res = word

        return res
