# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Approach
--------
two pointers: fast and slow
if they meet, there's a cycle

T: O(N)
S: O(1)
'''

'''
Notes
-----
1st attempt has some bug which I was not able to spot.

'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # base
        if not head:
            return False
        if not head.next:
            return False

        # code
        slow = head
        # [Miss] This is also a bug. fast should start at head and not head.next
        fast = head.next
        fast = head
        # while slow and fast: # [Miss] This while loop should be while fast and fast.next. Because if those two are true then slow.next will any be true
        while fast and fast.next:
            # [Miss] syntax error below
            # return True if slow == fast and repeat
            slow = slow.next
            # [Miss] syntax error below. Looks like I don't know how to use ternary operator properly
            # fast = fast.next.next if fast.next else return True
            # if fast.next: #[Miss] This is not required anymore since we are checking this in the while loop condition
            fast = fast.next.next
            if slow == fast:
                return True
            # [Miss] This else block is not needed. If slow is not equal to fast yet, we advance in the while loop.
            # else: 
            #     '''
            #     [Miss] This a major bug. It should be return False 
            #     because it means we reached the end of the list and 
            #     there's no cycle. The fact that not being able to find 
            #     this one and relying on Claude to find the bug is a 
            #     major red flag about lack of concentration.
            #     '''
            #     # return True
            #     return False
        return False

