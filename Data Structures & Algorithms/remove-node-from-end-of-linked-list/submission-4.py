# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        i1,i2 = dummy,dummy
        gap = 0
        while i1 and i2:
            i1 = i1.next
            gap += 1
            if gap > n+1:
                i2 = i2.next
            
        i2_nxt = None
        if i2 and i2.next:
            i2_nxt = i2.next.next
            i2.next.next = None
            i2.next = i2_nxt
        
        return dummy.next