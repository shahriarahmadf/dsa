/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    
    const mirror_checker = (root_left,root_right) => {
        if (root_left == null && root_right == null){
            return true;
        }
        else if (root_left != null & root_right != null){
            if (root_left.val == root_right.val){
                return mirror_checker(root_left.left,root_right.right) && mirror_checker(root_left.right,root_right.left);
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }

    if (root == null){
        return true;
    }
    else{
        return mirror_checker(root.left,root.right);
    }
};