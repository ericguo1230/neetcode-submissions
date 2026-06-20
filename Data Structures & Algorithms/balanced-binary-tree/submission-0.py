# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        right = self.height(root.right)
        left = self.height(root.left)
        if abs(right - left) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))