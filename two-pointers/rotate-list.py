# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k %= n
        if k == 0:
            return head
        curr = head
        for _ in range(n-k-1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        return new_head
        