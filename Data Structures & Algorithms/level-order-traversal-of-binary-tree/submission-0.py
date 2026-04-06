# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = []
        buf = []
        result = []
        q_len = 0

        if root:
            Q.append(root)
            q_len = 1

        while Q:
            cur_node = Q.pop()
            buf.append(cur_node)
            if cur_node.left:
                Q.insert(0, cur_node.left)
            if cur_node.right:
                Q.insert(0, cur_node.right)
            if len(buf) == q_len:
                result.append([x.val for x in buf])
                buf.clear()
                q_len = len(Q)
        return result

