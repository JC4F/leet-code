class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
    class Trie:
    
        def __init__(self):
            self.root = TrieNode()
    
        # @param {string} word
        # @return {void}
        # Inserts a word into the trie.
        def insert(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    node.children[i]=TrieNode()
                node=node.children[i]
            node.word=True
    
        # @param {string} word
        # @return {boolean}
        # Returns if the word is in the trie.
        def search(self, word):
            node=self.root
            for i in word:
                if i not in node.children:
                    return False
                node=node.children[i]
            return node.word
    
        # @param {string} prefix
        # @return {boolean}
        # Returns if there is any word in the trie
        # that starts with the given prefix.
        def startsWith(self, prefix):
            node=self.root
            for i in prefix:
                if i not in node.children:
                    return False
                node=node.children[i]
            return True
            
    
    # Your Trie object will be instantiated and called as such:
    # trie = Trie()
    # trie.insert("somestring")
    # trie.search("key")
    
class Trie:
    def __init__(self):
        # Root node with children and a flag indicating if it's the end of a word
        self.children = {}
        self.is_word = False

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self
        for char in word:
            # If the character is not in the children, add a new Trie node
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        # Mark the end of the word
        node.is_word = True

    def search(self, word):
        """Return True if the word is in the Trie, False otherwise."""
        node = self._find_node(word)
        # Check if we found the node and it's marked as a complete word
        return node is not None and node.is_word

    def starts_with(self, prefix):
        """Return True if there is any word in the Trie that starts with the given prefix."""
        # Check if the prefix exists in the Trie
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        """Helper method to traverse the Trie and return the node corresponding to the prefix."""
        node = self
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
