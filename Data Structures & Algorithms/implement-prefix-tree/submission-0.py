# first create an init class for adding node
# with have 1- child as a list or {} , 2-bool end_of_word

# second we need to just init at the prefix tree a root
# third for the insert 
# we need to have a curr node start with root
# and loop at every char if not in the child add a new node
# and after that make that end_of_word as true

# forth for the search do the same and the same with starts with
# I mean the same logic 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True        


    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.end_of_word # that mean it's a word or not        
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return True        
        
        