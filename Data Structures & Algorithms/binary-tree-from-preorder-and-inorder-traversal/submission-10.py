# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {val:idx for idx, val in enumerate(inorder)}
        l = 0
        r = len(inorder)-1
        self.idx = 0
        def dfs(l,r):
            if l > r:
                return
            root = TreeNode(preorder[self.idx])
            m = cache[root.val]
            self.idx += 1
            root.left = dfs(l, m - 1)
            root.right = dfs(m+1, r)
            return root

        return dfs(l,r)