# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break the list into two
        head2 = slow.next
        slow.next = None

        # reverse the new list
        prev = None
        cur = head2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev

        # interleave the two lists
        first,second = head,head2
        while first and second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2