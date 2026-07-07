# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break in the middle
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        # reverse the second list
        prev,cur = None,head2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev

        # interleave two lists
        first,second = head,head2
        while first and second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2