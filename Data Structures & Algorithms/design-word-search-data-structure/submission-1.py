class Node:

    def __init__(self):
        self.children = defaultdict(lambda: Node())
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            cur = cur.children[i]
        cur.endofword = True
        return
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    cur = cur.children[c]
            return cur.endofword
        return dfs(0, self.root)
        
