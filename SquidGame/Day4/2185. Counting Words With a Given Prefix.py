
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            count += pref == word[:len(pref)]
        return count

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.pref = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.pref += 1
        curr.isWord = True

    def getPrefixCount(self, pref)-> int:
        curr = self.root
        for ch in pref:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.pref

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.getPrefixCount(pref)



