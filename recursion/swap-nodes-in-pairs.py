# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        output = head.next
        prev = None
        curr = head
        while curr and curr.next:
            swap = curr.next
            after = swap.next
            if prev:
                prev.next, swap.next, curr.next = swap, curr, after
            else:
                swap.next, curr.next = curr, after
            prev = curr
            curr = curr.next
        return output