class TreeNode:
    def __init__(self, key:int, val:int, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return

        cur = self.root
        while True:
            if newNode.key < cur.key:
                if cur.left == None:
                    cur.left = newNode
                    return
                cur = cur.left
            elif newNode.key > cur.key:
                if cur.right == None:
                    cur.right = newNode
                    return
                cur = cur.right
            else:
                cur.val = val
                return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        return -1


    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur: TreeNode, key: int) -> TreeNode:
        if not cur:
            return None
        
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                # replace right child
                return cur.right
            elif not cur.right:
                # replace left child
                return cur.left
            else:
                # swap cur with inorder successor
                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        
        return cur



    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res

    def inorderTraversal(self, root: TreeNode, res: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, res)
            res.append(root.key)
            self.inorderTraversal(root.right, res)
        
        
