def search_in_binary_tree(tree_array,target):
    class Binary_Tree_Node:
        """This is Binary Tree Node under which all BST functions are defined"""

        def __init__(self,val):
            """Initialize a new Binary_Tree_Node with the given value"""
            self.val = val
            self.left = None
            self.right = None 

        def printer(self):
            """Prints a Node with its left and right value"""
            if self is None:
                print('nothing')
                return
            else:
                print(f'Node is {self.val}')
            if self.left is None:
                print('nothing on left')
            else:
                print(f'Node.left is {self.left.val}')
            if self.right is None:
                print('nothing on right')
            else:
                print(f'Node.right is {self.right.val}')
        
        def insert(self,new_val):
            """Inserts a new Node once root is defined"""
            if new_val < self.val:
                if self.left is None:
                    self.left = Binary_Tree_Node(new_val)
                else:
                    self.left.insert(new_val)
            else:
                if self.right is None:
                    self.right = Binary_Tree_Node(new_val)
                else:
                    self.right.insert(new_val)
        
        def inorder_traversal_target(self,target):
            """Finds the target node through inorder traversal"""
            if self.left:
                x = self.left.inorder_traversal_target(target)
                if x is not None:
                    return x

            if target == self.val:
                return self

            if self.right:
                y = self.right.inorder_traversal_target(target)
                if y is not None:
                    return y

        def array_to_tree(tree_array):
            """Coverts array input to tree"""
            for i in range(len(tree_array)): 
                if i == 0:
                    root = Binary_Tree_Node(tree_array[i])
                else:
                    root.insert(tree_array[i])
            return root
        
    root = Binary_Tree_Node.array_to_tree(tree_array)
    # Uncomment the line below if you want to see the root node with its left and right
    #Binary_Tree_Node.printer(root)

    target_subtree = None
    target_subtree = root.inorder_traversal_target(target)

    # Uncomment the line below if you want to see the target subtree root node with its left and right
    #Binary_Tree_Node.printer(target_subtree)

    return target_subtree

print(search_in_binary_tree( [4,2,7,1,3], 2))

# Time complexity: log(n)
# Space complexity: O(n)
