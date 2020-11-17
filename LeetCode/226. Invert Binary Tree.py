# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def inorder(cur_node: TreeNode):
            if not cur_node:
                return

            cur_node.left, cur_node.right = cur_node.right, cur_node.left
            inorder(cur_node.left)
            inorder(cur_node.right)

        inorder(root)
        return root
