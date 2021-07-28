package ink.chow.leetcode.algorithm;

public class Problems24SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        if (head.next == null) {
            return head;
        }
        ListNode newHead = new ListNode();
        ListNode pre = null;
        ListNode temp;
        ListNode end = newHead;
        while (head != null) {
            if (pre == null) {
                pre = head;
                head = head.next;
            } else {
                end.next = head;
                temp = head.next;
                head.next = pre;
                end = pre;
                pre.next = null;
                head = temp;
                pre = null;
            }
        }
        if (pre != null) {
            end.next = pre;
        }
        return newHead.next;
    }
}
