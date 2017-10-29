class TrieNode(object):
    def __init__(self, char):
        """
        Initialize your data structure here.
        """
        self.character = char
        self.isWord = False
        self.children = [None] * 26

class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root

        for char in word:
            pos = ord(char) - ord('a')
            if current.children[pos] == None:
                current.children[pos] = TrieNode(char)

            current = current.children[pos]

        current.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            pos = ord(char) - ord('a')
            if node.children[pos] == None:
                return False
            else:
                node = node.children[pos]

        return node.isWord


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root

        for char in prefix:
            pos = ord(char) - ord('a')
            if node.children[pos] == None:
                return False
            else:
                node = node.children[pos]

        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("ab")
# trie.search("a")