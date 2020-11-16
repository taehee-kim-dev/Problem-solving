# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.answer = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0

        def preorder(cur_node: TreeNode, cur_binary_str: str = '') -> None:
            if not cur_node.left and not cur_node.right:
                self.answer.append(int(cur_binary_str + str(cur_node.val), 2))
                return

            if cur_node.left:
                preorder(cur_node.left, cur_binary_str + str(cur_node.val))
            if cur_node.right:
                preorder(cur_node.right, cur_binary_str + str(cur_node.val))

        preorder(root)
        return sum(self.answer)
