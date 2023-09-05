class Node:
    """Represents a Node in a Linked List"""
    
    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)
class LinkedList:
    """Represents a Single Linked List"""

    def __init__(self):
        self.head = None

    def add(self, new_item):
        """Creates a new Node with 'new_item' and adds to the front"""

        node = Node(new_item)
        node.next = self.head
        self.head = node
        return self.head
    
    def delete(self, item):
        """Deletes the target item or Node from the Linked List, if exists"""
        # case 0: delete head
        if self.head.data == item:
            self.head = self.head.next
            return self.head
        
        # case 1: delete a middle Node
        prev = None
        curr = self.head
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        
        if curr: # case 2: item not found case handled with this condition
            prev.next = curr.next
        return self.head

    def __str__(self):
        """Returns a String that represents all the Nodes from head in the Linked List"""
        output = []
        curr = self.head
        while curr:
            output.append(curr.data)
            curr = curr.next
        return str(output)
    
llist = LinkedList()
llist.add(5)
llist.add(10)
llist.add(15)
print(llist)
llist.delete(15) 
print(llist)
