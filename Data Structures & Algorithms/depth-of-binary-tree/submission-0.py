# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode]) -> int:
        # base case(s)
        if not root:
            return 0

        # code
        l_depth = self.helper(root.left)
        r_depth = self.helper(root.right)

        # depth = math.max(l_depth, r_depth) + 1
        # [Notes] It's not math.max. Just max
        depth = max(l_depth, r_depth) + 1
        return depth 

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)
        