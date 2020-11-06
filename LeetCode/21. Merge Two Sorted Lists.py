# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        merged_node_head = None
        last_node_of_merged_node = None
        l1_current_node = l1
        l2_current_node = l2

        while l1_current_node is not None and l2_current_node is not None:
            next_node = l1_current_node if l1_current_node.val <= l2_current_node.val else l2_current_node

            if merged_node_head is None:
                merged_node_head = next_node
                last_node_of_merged_node = next_node
            else:
                last_node_of_merged_node.next = next_node
                last_node_of_merged_node = next_node

            if next_node is l1_current_node:
                l1_current_node = l1_current_node.next
            else:
                l2_current_node = l2_current_node.next

        if l1_current_node is not None or l2_current_node is not None:
            remaining_list_current_node = l1_current_node if l1_current_node is not None else l2_current_node

            while remaining_list_current_node is not None:
                last_node_of_merged_node.next = remaining_list_current_node
                last_node_of_merged_node = remaining_list_current_node

                remaining_list_current_node = remaining_list_current_node.next

        return merged_node_head


node1_for_l1 = ListNode(1)
node2_for_l1 = ListNode(2)
node3_for_l1 = ListNode(4)

node1_for_l2 = ListNode(1)
node2_for_l2 = ListNode(3)
node3_for_l2 = ListNode(4)

l1_head = node1_for_l1
node1_for_l1.next = node2_for_l1
node2_for_l1.next = node3_for_l1

l2_head = node1_for_l2
node1_for_l2.next = node2_for_l2
node2_for_l2.next = node3_for_l2

solution = Solution()
solution.mergeTwoLists(l1_head, l2_head)
print('test')
