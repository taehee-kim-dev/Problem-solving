# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_count = 1
        l2_count = 1
        l1_num = 0
        l2_num = 0

        while l1:
            l1_num += l1.val * l1_count
            l1_count *= 10
            l1 = l1.next

        while l2:
            l2_num += l2.val * l2_count
            l2_count *= 10
            l2 = l2.next

        nums_sum = l1_num + l2_num
        reversed_sum_str = str(nums_sum)[::-1]
        result_head = ListNode(int(reversed_sum_str[0]))
        current_node = result_head

        for num_char in reversed_sum_str[1:]:
            current_node.next = ListNode(int(num_char))
            current_node = current_node.next

        return result_head


l1_1 = ListNode(0)

l2_1 = ListNode(0)

solution = Solution()
solution.addTwoNumbers(l1_1, l2_1)
