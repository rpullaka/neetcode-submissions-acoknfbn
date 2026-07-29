# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return root

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        l_lca = self.lowestCommonAncestor(root.left, p, q)
        if l_lca:
            return l_lca
        r_lca = self.lowestCommonAncestor(root.right, p, q)
        if r_lca:
            return r_lca
        
        return None