class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode((l1.val + l2.val)%10)
        carry = (l1.val + l2.val)//10
        index = head
        while True:
            if l1.next is None and l2.next is None:
                break
            else:
                if l1.next is None:
                    l1.next = ListNode(0)
                if l2.next is None:
                    l2.next = ListNode(0)
                index.next = ListNode((l1.next.val + l2.next.val + carry)%10)
                carry = (l1.next.val + l2.next.val+carry)//10
                l1 = l1.next
                l2 = l2.next
                index = index.next
        if carry:
            index.next = ListNode(carry)
        return head