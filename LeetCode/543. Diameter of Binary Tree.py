# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.current_max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def max_depth(cur_node: TreeNode) -> int:
            if not cur_node:
                return 0
            # 반환값 : 현재 노드부터 리프노드들까지 경로를 봤을 때, 최대 깊이값
            max_depth_of_left_child_nodes = max_depth(cur_node.left)
            max_depth_of_right_child_nodes = max_depth(cur_node.right)
            self.current_max_diameter \
                = max(self.current_max_diameter,
                      max_depth_of_left_child_nodes + max_depth_of_right_child_nodes)

            return 1 + max(max_depth_of_left_child_nodes, max_depth_of_right_child_nodes)

        max_depth(root)
        return self.current_max_diameter

