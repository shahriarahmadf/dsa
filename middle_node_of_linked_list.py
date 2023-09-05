# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_oneStep = head
        curr_twoStep = head

        while curr_twoStep:

            if curr_twoStep.next == None:
                break
            curr_twoStep = curr_twoStep.next.next
            curr_oneStep = curr_oneStep.next
        
        return curr_oneStep