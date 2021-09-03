from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l2 if l1 is None else l1
        else:
            result = []
            while l1:
                result.append(l1.val)
                l1 = l1.next
            while l2:
                result.append(l2.val)
                l2 = l2.next
        result.sort()
        head = ListNode(result[0])
        index = head
        for num in result[1:]:
            index.next = ListNode(num)
            index = index.next
        return head

