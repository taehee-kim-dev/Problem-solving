# Definition for singly-linked list.
import collections
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        deque: Deque = collections.deque()

        node = head
        while node is not None:
            deque.append(node.val)
            node = node.next

        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False

        return True

