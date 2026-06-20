# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(maxi, root):
            if not root:
                return 0
            
            if root.val >= maxi:
                return 1 + dfs(root.val, root.right) + dfs(root.val, root.left)
            else:
                return dfs(maxi, root.right) + dfs(maxi, root.left)
        
        return dfs(-100, root) if root else 0
