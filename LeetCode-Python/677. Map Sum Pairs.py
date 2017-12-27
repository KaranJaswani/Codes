class TrieNode(object):
    def __init__(self, char, value):
        self.character = char
        self.value = value
        self.isWord = False
        self.children = [None] * 26

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('', 0)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        current = self.root
        
        isPresent = self.search(key)
        
        for char in key:
            pos = ord(char) - ord('a')
            if current.children[pos] == None:
                current.children[pos] = TrieNode(char, val)
            else:
                if isPresent:
                    current.children[pos].value = val
                else:
                    current.children[pos].value += val
                
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
    
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if current != None:
                current = current.children[pos]
            else:
                return 0
        
        return current.value if current != None else 0
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)