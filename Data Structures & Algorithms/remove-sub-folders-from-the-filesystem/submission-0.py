class Node:
    def __init__(self, end: bool = False):
        self.children = {}
        self.end = end

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, directory: str):
        cur = self.root
        items = directory[1:].split('/')
        print(items)
        valid = True
        for item in items:
            if not item:
                valid = False
                break
            if item not in cur.children:
                cur.children[item] = Node()
            cur = cur.children[item]
        if valid:
            cur.end = True

    def search(self, directory) -> bool:
        cur = self.root
        items = directory[1:].split('/')
        for item in items:
            if cur.end or not item:
                return False
            cur = cur.children[item]
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for directory in folder:
            trie.insert(directory)
        
        for directory in folder:
            if trie.search(directory):
                res.append(directory)
        return res
