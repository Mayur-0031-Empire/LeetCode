# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        curr_sum = 0
        max_sum = float("-inf")
        curr_level = 0
        max_level = 0
    
        while dq:
            l = len(dq)
            curr_sum = 0
            for i in range(l):
                node = dq.popleft()
                curr_sum += node.val
                if node.right:
                    dq.append(node.right)
                if node.left :
                    dq.append(node.left)

            curr_level += 1
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level
        
        return max_level

        