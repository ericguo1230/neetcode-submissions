# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def _treeToArray(self, root):
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result

    def __init__(self, root: Optional[TreeNode]):
        #In order traversal of tree expressed as an array
        self.arr = self._treeToArray(root)
        self.idx = 0

    def next(self) -> int:
        #Return current index
        #increment by 1
        if not self.arr or self.idx >= len(self.arr):
            return -1
        ans = self.arr[self.idx]
        self.idx += 1
        return ans


    def hasNext(self) -> bool:
        #return whether or not idx + 1 < len(array)
        return self.idx < len(self.arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()