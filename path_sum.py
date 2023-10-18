# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # if root is None, return False
        if root is None:
            return False
        
        # check if we have reached the leaf
        if root.left is None and root.right is None:
            return targetSum==root.val

        # if not, we go towards leaf
        else:
            return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val) # either edge towards leaf if sum gives zero, we return True
