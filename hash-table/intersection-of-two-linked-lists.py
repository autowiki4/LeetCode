# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Loop through the first list
# store the nodes in the first list in a hashmap
# lopp through the second list while checking if the
# set
# return the node if found. else return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = lenB = 0
        lastA = lastB = None

        ptr = headA
        while ptr:
            lenA += 1
            lastA = ptr
            ptr = ptr.next

        ptr = headB
        while ptr:
            lenB += 1
            lastB = ptr
            ptr = ptr.next

        if lastA != lastB:
            return None

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

# Runtime: O(n) where n is thenumber of items in the longest
# SPace complexity: O(n)