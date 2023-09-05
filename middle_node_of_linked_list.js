/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let oneStepper = head;
    let twoStepper = head;

    while (twoStepper){
        if (twoStepper.next == null){
            break;
        }
        oneStepper = oneStepper.next;
        twoStepper = twoStepper.next.next;
    }
    return oneStepper;
};