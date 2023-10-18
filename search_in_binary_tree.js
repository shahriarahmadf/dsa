function searchInBinaryTree(treeArray,target){

    class BinaryTreeNode {
        
        // constructor definition for each Node
        constructor(val){
            this.val = val;
            this.left = null;
            this.right = null;
        }

        // inserts a new Node once root is defined
        insert(new_val){
            if (new_val < this.val) {
                if (this.left === null) {
                    this.left = new BinaryTreeNode(new_val);
                }
                else{
                    this.left.insert(new_val);
                }
            }
            else{
                if(this.right === null) {
                    this.right = new BinaryTreeNode(new_val);
                }
                else {
                    this.right.insert(new_val);
                }
            }
        }

        // finds the target Node through inorder traversal
        inorderTraversalNode(target){
            if (this.left != null) {
                const left = this.left.inorderTraversalNode(target);
                if (left != null){
                    return left;
                }
            }
            if (target == this.val){
                return this;
            }
            if (this.right != null) {
                const right = this.right.inorderTraversalNode(target);
                if (right != null) {
                    return right;
                }
            }
        }

        // converts input array to BST
        arrayToTree(array){
            const root = new BinaryTreeNode(array[0])
            for (let i=1; i<array.length; i++){
                root.insert(array[i]);
            }
            return root;
        }

    // end of BST class
    }

    // handle function input

    const binaryTree = new BinaryTreeNode();
    const root = binaryTree.arrayToTree(treeArray);

    let targetSubtree = null;
    targetSubtree = root.inorderTraversalNode(target);

    return targetSubtree;
}

console.log(searchInBinaryTree([4,2,7,1,3],2));

// Time complexity: log(n)
// Space complexity: O(n)
