"""
길 찾기 게임
"""

import sys
sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.left_child_node = None
        self.right_child_node = None


def insert_node(parent_node, child_node):
    if child_node.x < parent_node.x:
        if parent_node.left_child_node is None:
            parent_node.left_child_node = child_node
        else:
            insert_node(parent_node.left_child_node, child_node)
    else:
        if parent_node.right_child_node is None:
            parent_node.right_child_node = child_node
        else:
            insert_node(parent_node.right_child_node, child_node)


def pre_order(node, pre_order_result):
    if node is None:
        return
    else:
        pre_order_result.append(node.number)
        pre_order(node.left_child_node, pre_order_result)
        pre_order(node.right_child_node, pre_order_result)


def post_order(node, post_order_result):
    if node is None:
        return
    else:
        post_order(node.left_child_node, post_order_result)
        post_order(node.right_child_node, post_order_result)
        post_order_result.append(node.number)


def solution(nodeinfo):
    nodes = []
    for number, info in enumerate(nodeinfo, 1):
        nodes.append(Node(number, info[0], info[1]))

    nodes.sort(key=lambda one_node: [-one_node.y, one_node.x])

    root_node = nodes[0]

    for node in nodes[1:]:
        insert_node(root_node, node)

    pre_order_result = []
    pre_order(root_node, pre_order_result)

    post_order_result = []
    post_order(root_node, post_order_result)

    return [pre_order_result, post_order_result]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
