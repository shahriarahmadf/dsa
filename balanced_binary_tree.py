# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def calculateHeight(root):
            if root is None:
                return 0
            left_height = calculateHeight(root.left) 
            right_height = calculateHeight(root.right) 
            return 1 + max(left_height,right_height)
        
        if root is None:
            return True
        
        left_height = calculateHeight(root.left)
        right_height = calculateHeight(root.right)

        if abs(left_height-right_height) > 1:
            return False
        
        if not (self.isBalanced(root.left)):
            return False
        
        if not (self.isBalanced(root.right)):
            return False
        return True

