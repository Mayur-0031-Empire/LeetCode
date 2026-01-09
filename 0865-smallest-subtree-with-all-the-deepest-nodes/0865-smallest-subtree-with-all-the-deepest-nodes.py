# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS(r, level):
            if not r.left and not r.right:
                return [r, level]
            left = [None, -1]
            right = [None, -1]
            if r.left:
                left = DFS(r.left, level + 1)
            if r.right :
                right = DFS(r.right, level + 1)
            # print(left, right)
                
            if left[-1] == right[-1]:
                return [r, left[-1]]
            
            if left[1] > right[1]:
                return left
            else :
                return right
        
        ans = DFS(root, 1)
        return ans[0]
            
            
            

        