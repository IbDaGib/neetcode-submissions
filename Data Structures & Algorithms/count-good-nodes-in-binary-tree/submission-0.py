# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        cur = root
        def dfs(cur, maxi):
            nonlocal res
            if not cur:
                return 0
            if cur.val >= maxi:
                res += 1
            maxi = max(maxi, cur.val)
            left = dfs(cur.left, maxi)
            right = dfs(cur.right, maxi)
            return res
        
        return dfs(cur, root.val)