# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        pointer = dummy
        while l1 or l2 or carry:
            curr = carry
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            carry = curr // 10
            curr = curr % 10
            pointer.next = ListNode(val=curr)
            pointer = pointer.next
        return dummy.next
        