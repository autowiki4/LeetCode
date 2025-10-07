# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        if n == 1:
            return None
        m = n // 2
        curr = head
        for i in range(m - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head