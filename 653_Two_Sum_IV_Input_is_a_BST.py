# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                ans.append(root.val)
                inOrder(root.right)
        ans = []
        inOrder(root)
        l, r = 0, len(ans)-1
        while l< r:
            if ans[l]+ans[r] > k:
                r -=1
            elif ans[l]+ans[r] < k:
                l +=1
            else: 
                return True
        return False
