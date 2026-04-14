# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums):
            if not nums:
                return None
            max_val = max(nums)
            new_head = TreeNode(max_val)
            idx = nums.index(max_val)
            new_head.left = build(nums[:idx])
            new_head.right = build(nums[idx+1:])
            return new_head
        return build(nums)
