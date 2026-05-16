"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # clone = {}

        # def dfs(node):
        #     if node in clone:
        #         return clone[node]
            
        #     copy = Node(node.val)
        #     clone[node] = copy
        #     for n in node.neighbors:
        #         copy.neighbors.append(dfs(n))
        #     return copy
        
        # return dfs(node) if node else None

        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                    q.append(n)
                clone[cur].neighbors.append(clone[n])
        
        return clone[node]
        