# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        is_node_same = (p and q and (p.val == q.val))
        if not is_node_same:
            return False
        is_left_same = self.isSameTree(p.left, q.left)
        if not is_left_same:
            return False
        is_right_same = self.isSameTree(p.right, q.right)
        if not is_right_same:
            return False
        return True

'''
Test Cases
----------

'''