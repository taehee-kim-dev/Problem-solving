from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        if not root:
            return answer

        stack = [root]
        while stack:
            curr_node = stack.pop()
            answer.append(curr_node.val)
            if curr_node.children:
                stack.extend(curr_node.children)

        return answer[::-1]
