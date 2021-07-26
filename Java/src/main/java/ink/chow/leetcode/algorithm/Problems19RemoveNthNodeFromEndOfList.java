package ink.chow.leetcode.algorithm;

public class Problems19RemoveNthNodeFromEndOfList {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int counter = 1;
        ListNode right = head;
        while (counter < n && right != null) {
            right = right.next;
            counter ++;
        }
        if (right == null) {
            return null;
        }
        ListNode left = head;
        ListNode pre = null;
        while (right.next != null) {
            right = right.next;
            pre = left;
            left = left.next;
        }
        if (pre != null) {
            pre.next = left.next;
        } else {
            head = left.next;
        }
        left.next = null;
        return head;
    }

    public static void main(String[] args) {
        System.out.println(
                ListNode.listNodeToString(
                new Problems19RemoveNthNodeFromEndOfList().removeNthFromEnd(ListNode.stringToListNode("[1,2,3,4,5]"), 2)));
    }
}
