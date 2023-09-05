/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {

    // use a dummy head to avoid edge case issues
    let dummyHead = new ListNode(0,head);

    let leftPrev = dummyHead;
    let curr = head;

    for (let i=1; i<left; i++){
        leftPrev = curr;
        curr = curr.next;
    }

    // reverse the list Nodes between Left and Right
    let prev = null;
    for (let i = left; i<= right; i++){
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }
    // end of loop, prev = right position element, curr = first element after right.
    
    // update the first Node of the reversing list to point to first element after right
    leftPrev.next.next = curr;
    // update the Node just before Left to point to the Right Node
    leftPrev.next = prev;

    // return the Node List next to our dummyHead
    return dummyHead.next;
};

// Time complexity: O(right+1)
// Space complexity: O(1)
