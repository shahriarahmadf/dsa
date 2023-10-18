class Node:
    def __init__(self,value):
        """A node in the Tree"""
        self.left = None
        self.val = value
        self.right = None

class Tree:
    def createNode(self,data):
        """Create a Node in Tree"""
        # data = [val, left, right]
        return Node(data)
    
    def insert(self,current_node,data):
        """Insert a value as a Node inside the Tree"""
        if current_node is None:
            return self.createNode(data)
        else:
            if data < current_node:
                return self.insert(current_node.left,data)
            else:
                return self.insert(current_node.right,data)
    