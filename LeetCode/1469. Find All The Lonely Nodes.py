# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        answer = []

        def preorder(cur_node: TreeNode):
            if not cur_node:
                return

            if cur_node.left and not cur_node.right:
                answer.append(cur_node.left.val)
            elif not cur_node.left and cur_node.right:
                answer.append(cur_node.right.val)

            preorder(cur_node.left)
            preorder(cur_node.right)

        preorder(root)
        return answer
