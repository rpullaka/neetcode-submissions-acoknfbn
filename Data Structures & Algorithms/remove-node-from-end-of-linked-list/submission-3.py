# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow,fast = dummy,head
        i = 0
        while fast:
            if i >= n:
                slow = slow.next
            fast = fast.next
            i += 1
        if n > i:
            return head
        if slow and slow.next:
            temp = slow.next
            slow.next = temp.next
            temp.next = None
        return dummy.next
            