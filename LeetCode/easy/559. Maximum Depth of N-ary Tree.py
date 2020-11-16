
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.cur_max_depth = 0

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def dfs(cur_node: Node, cur_depth: int):
            if not cur_node.children:
                self.cur_max_depth = max(self.cur_max_depth, cur_depth)
                return

            for next_node in cur_node.children:
                dfs(next_node, cur_depth + 1)

        dfs(root, 1)
        return self.cur_max_depth
