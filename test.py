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


# Example usage:
trie = Trie()
trie.insert("somestring")
print(trie.search("somestring"))  # Output: True
print(trie.search("key"))  # Output: False
print(trie.starts_with("some"))  # Output: True

"""
public int kthSmallest(TreeNode root, int k) {
      int count = countNodes(root.left);
      if (k <= count) {
          return kthSmallest(root.left, k);
      } else if (k > count + 1) {
          return kthSmallest(root.right, k-1-count); // 1 is counted as current node
      }
      
      return root.val;
  }
  
  public int countNodes(TreeNode n) {
      if (n == null) return 0;
      
      return 1 + countNodes(n.left) + countNodes(n.right);
  }
"""
