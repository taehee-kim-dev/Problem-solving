# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        def dfs(node: TreeNode):
            if not node:
                return 0
            if L <= node.val <= R:
                return dfs(node.left) + node.val + dfs(node.right)
            if node.val < L:
                return dfs(node.right)
            if R < node.val:
                return dfs(node.left)

        return dfs(root)
