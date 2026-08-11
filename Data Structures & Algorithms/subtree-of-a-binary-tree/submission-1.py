# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1 and root2:
                return root1.val == root2.val and is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
            return False
        
        def is_subtree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1:
                return False
            if is_same(root1, root2):
                return True
            return is_subtree(root1.left, root2) or is_subtree(root1.right, root2) 
        
        return is_subtree(root, subRoot)
