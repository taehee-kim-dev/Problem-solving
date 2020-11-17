# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        prev_node = None
        before_node = head
        after_node = before_node.next
        next_node = after_node.next

        before_node.next = next_node
        after_node.next = before_node
        head = after_node

        while next_node is not None and next_node.next is not None:
            prev_node = before_node
            before_node = before_node.next
            after_node = before_node.next
            next_node = after_node.next

            before_node.next = next_node
            after_node.next = before_node
            prev_node.next = after_node

        return head


node_1 = ListNode(1)

solution = Solution()
solution.swapPairs(node_1)
print('test')