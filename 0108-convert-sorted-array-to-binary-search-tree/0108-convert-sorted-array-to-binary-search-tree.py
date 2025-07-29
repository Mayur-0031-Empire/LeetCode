# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeBST(self, nums, start, end): 
        # base case
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.makeBST(nums, start, mid - 1)
        root.right = self.makeBST(nums, mid + 1, end)

        # if left:
        #     root.left = left
        # if right:
        #     root.right = right
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1
        return self.makeBST(nums, start, end)