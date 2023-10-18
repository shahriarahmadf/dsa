# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirror_checker(root_left,root_right):
            if root_left is not None and root_right is not None:
                if root_left.val == root_right.val:
                    return mirror_checker(root_left.left,root_right.right) and mirror_checker(root_left.right,root_right.left)
                else:
                    return False
            elif root_left is None and root_right is None:
                return True
            else:
                return False            
        
        if root is None:
            return True
        else:
            return mirror_checker(root.left,root.right)

