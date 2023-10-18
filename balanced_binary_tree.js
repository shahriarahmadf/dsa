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
var isBalanced = function(root) {
    
    function calculateHeight(root){
        if (root == null){
            return 0;
        }
        const left_height = calculateHeight(root.left);
        const right_height = calculateHeight(root.right);

        return 1 + Math.max(left_height,right_height);
    }

    if (root == null){
        return true;
    }
    const left_height = calculateHeight(root.left);
    const right_height = calculateHeight(root.right);

    if (Math.abs(left_height - right_height) > 1){
        return false;
    }

    if ( !isBalanced(root.left) || !isBalanced(root.right) ){
        return false;
    }

    return true;
};