# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {val: idx for idx, val in enumerate(inorder)}
        l, r = 0, len(inorder)-1
        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            mid = cache[root.val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(l,r)