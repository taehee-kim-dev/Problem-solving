from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        if not root:
            return answer

        stack = [root]
        while stack:
            cur_node = stack.pop()
            answer.append(cur_node.val)
            stack += cur_node.children[::-1]

        return answer
