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

'''
Time Complexity: O(N){iterate N elements} + O(N) {Clear total N elements from the buffer at line 28}
Space Complexity: O(N){Max Q length is N} + O((N + 1)/2) {Max buf length is the no of leaf nodes}
'''

'''
Apparently, time complexity is wrong. It is O(N^2) because list insert operation is O(N).
Better approach is to use a deque.
'''
