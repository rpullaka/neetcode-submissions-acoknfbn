# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [Notes] Got the below line wrong the first time. Didn't enclose the tuple in brackets and didn't check for list1 and list2.
        '''
        (L1,L2) = (list1,list2) if list1 and list2 and list1.val < list2.val else (list2,list1)
        # [Notes] Actually the above line is totally unnecessary.
        list3 = ListNode()
        L3 = list3
        while L1 and L2:
            if L1.val < L2.val:
                L3.next = L1
                L1 = L1.next
            else:
                L3.next = L2
                L2 = L2.next
            L3 = L3.next
        
        # if L1:
        #     L3.next = L1
        # else:
        #     L3.next = L2
        # [Notes] The above block can be simplified as below
        L3.next = L1 or L2
            
        return list3.next


        