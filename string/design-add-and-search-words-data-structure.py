class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # insert
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        # search
        def dfs(index, node): # return boolean
            print(index)
            curr = node
            # current index in word
            # if see ., check every child path 
            # from each child, check using new search
            # if no path, return False
            if index >= len(word):
                return curr.is_end
            if word[index] == '.' :
                for child in curr.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if word[index] not in curr.children:
                    return False
                # curr = curr.children[word[index]]
                return dfs(index + 1, curr.children[word[index]])

        return dfs(0, self.root)

    #         root
    # b         d         m
    # a         a         a
    # d         d         d
    # *         *         *

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)