# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        answer_head = None

        odds_head = None
        odds_last_node = None

        evens_head = None
        evens_last_node = None

        count = 1
        while head is not None:
            if count % 2 != 0:
                if odds_head is None and odds_last_node is None:
                    odds_head = head
                else:
                    odds_last_node.next = head
                odds_last_node = head
            else:
                if evens_head is None and evens_last_node is None:
                    evens_head = head
                else:
                    evens_last_node.next = head
                evens_last_node = head

            head = head.next
            count += 1

        answer_head = odds_head
        odds_last_node.next = evens_head
        if evens_last_node is not None:
            evens_last_node.next = None

        return answer_head


node_1 = ListNode(1)

solution = Solution()
solution.oddEvenList(node_1)
print('test')
