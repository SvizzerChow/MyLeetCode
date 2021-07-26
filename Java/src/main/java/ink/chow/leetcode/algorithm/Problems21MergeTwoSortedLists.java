package ink.chow.leetcode.algorithm;

public class Problems21MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode temp = result;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                temp.next = l1;
                l1 = l1.next;
                temp = temp.next;
                temp.next = null;
            } else {
                temp.next = l2;
                l2 = l2.next;
                temp = temp.next;
                temp.next = null;
            }
        }
        while (l1 != null) {
            temp.next = l1;
            l1 = l1.next;
            temp = temp.next;
            temp.next = null;
        }
        while (l2 != null) {
            temp.next = l2;
            l2 = l2.next;
            temp = temp.next;
            temp.next = null;
        }
        return result.next;
    }

}
