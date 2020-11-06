# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_number_in_str = '0b'
        while head is not None:
            binary_number_in_str += str(head.val)
            head = head.next

        return int(binary_number_in_str, 2)

