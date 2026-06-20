# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        dp = {}
        
        def dfs(node, rob):
            if (node, rob) in dp:
                return dp[(node, rob)]
            if node.left is None and node.right is None:
                return node.val if rob else 0
            elif node.left is None:
                if rob:
                    dp[(node, rob)] = max(dfs(node.right, not rob) + node.val, dfs(node.right, rob))
                else:
                    dp[(node, rob)] = dfs(node.right, not rob)
            elif node.right is None:
                if rob:
                    dp[(node, rob)] = max(dfs(node.left, not rob) + node.val, dfs(node.left, rob))
                else:
                    dp[(node, rob)] = dfs(node.left, not rob)
            else:
                if rob:
                    dp[(node, rob)] = max(dfs(node.right, not rob) + node.val + dfs(node.left, not rob),
                        dfs(node.right, rob) + dfs(node.left, rob))
                else:
                    dp[(node, rob)] = dfs(node.right, not rob) + dfs(node.left, not rob)
            return dp[(node, rob)]
        return dfs(root, True)
            