# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        curr = prev.next
        dummy = prev
        while prev and curr:
            if prev.val == curr.val:
                prev.next, curr = curr.next, curr.next
            else:
                prev = prev.next
                curr = curr.next
        return dummy

