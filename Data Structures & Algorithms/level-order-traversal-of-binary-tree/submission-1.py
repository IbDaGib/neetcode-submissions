# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        if root:
            q.append(root)

        while q:
            sublist = []
            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    sublist.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if sublist: 
                res.append(sublist)

        return res
