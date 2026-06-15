# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Notes
-----
1st attempt is wrong code. All test cases failed. Tried validating using test case before running for the 1st time but obviously did something wrong.
2nd attempt: Got it correct by fluke. Still don't fully understand the logic.

[Weakness] Struggling with the index movement while navigating a list.
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # base case(s)
        if not head:
            return head

        # code
        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = dummy

        i = 0
        while right.next:
            # [Problem] I think it's super confusing to move the right point and increment i at separate places. We should try to do these together like an atomic thing.
            # right = right.next
            # if i >= n:
            #     left = left.next
            # i += 1
            if i >= n:
                left = left.next
            right = right.next
            i += 1      
            
        if i < n:
            return dummy.next

        if left and left.next:
            # this is the Nth node from the end
            temp = left.next.next
            left.next = temp
            # left.next.next = None
        
        return dummy.next

'''
Test Case
----------
L = [1, 2, 3, 4, 5, 6]
n = 3


'''