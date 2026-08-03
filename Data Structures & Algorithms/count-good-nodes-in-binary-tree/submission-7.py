# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        maxi = float('-inf')
        def dfs(root, maxi):
            if not root:
                return None
            if root.val >= maxi:
                self.res += 1
            maxi = max(root.val, maxi)
            dfs(root.left, maxi)
            dfs(root.right, maxi)
        
        dfs(root, maxi)
        return self.res