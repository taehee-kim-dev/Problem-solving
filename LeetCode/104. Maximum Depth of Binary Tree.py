# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cur_max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        def dfs(cur_node, cur_depth):
            if not cur_node:
                self.cur_max_depth = max(self.cur_max_depth, cur_depth - 1)
                return

            dfs(cur_node.left, cur_depth + 1)
            dfs(cur_node.right, cur_depth + 1)

        dfs(root, 1)
        return self.cur_max_depth