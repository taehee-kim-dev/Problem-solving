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
            # 반환값 : 현재 노드부터 리프노드들까지 최대 경로
            # 왼쪽 자식 노드를 시작으로
            max_depth_of_left_child_nodes = max_depth(cur_node.left)
            # 오른쪽 자식 노드를 시작으로
            max_depth_of_right_child_nodes = max_depth(cur_node.right)
            # 두 개 합치면 현재 노드를 기준으로 경로 형성. 더하기만 하면 됨.
            # 경로는 사이 간선의 개수이기 때문.
            self.current_max_diameter \
                = max(self.current_max_diameter,
                      max_depth_of_left_child_nodes + max_depth_of_right_child_nodes)

            # 반환값은, 현재 노드를 포함한 경로에 대한 경로 길이값을
            # 상위함수에 있는 부모 노드에게 전달해야 하므로, 1을 더해서 반환한다.
            return 1 + max(max_depth_of_left_child_nodes, max_depth_of_right_child_nodes)

        max_depth(root)
        return self.current_max_diameter

