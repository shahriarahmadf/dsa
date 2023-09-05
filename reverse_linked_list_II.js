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
    let dummyHead = new ListNode(0,head);

    let leftPrev = dummyHead;
    let curr = head;

    for (let i=1; i<left; i++){
        leftPrev = curr;
        curr = curr.next;
    }

    let prev = null;
    for (let i = left; i<= right; i++){
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }
    leftPrev.next.next = curr;
    leftPrev.next = prev;

    return dummyHead.next;
};