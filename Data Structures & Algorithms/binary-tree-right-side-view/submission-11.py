# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        def dfs(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append(root.val)
            if root.right:
                dfs(root.right, depth + 1)
            if root.left:
                dfs(root.left, depth + 1)
            return
        dfs(root, 0)
        return res
        # q = deque([root])
        # while q:
        #     rightSide = None
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         rightSide = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(rightSide.val)
        # return res

