# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, flag):
            if not root:
                return (0, True)

            left = dfs(root.left, True)
            right = dfs(root.right, True)

            if abs(left[0]-right[0]) > 1 or left[1] == False or right[1] == False:
                return (0, False)
            else:
                return (max(left[0], right[0])+1, True)

        return dfs(root, True)[1]