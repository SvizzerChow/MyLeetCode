package ink.chow.leetcode.algorithm;

/**
 * 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
 * 请你将两个数相加，并以相同形式返回一个表示和的链表。
 * 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/add-two-numbers
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
public class Problems2AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        ListNode end = result;
        int temp = 0;
        while (l1 != null && l2 != null){
            int val = l1.val + l2.val + temp;
            temp = val / 10;
            if (val >= 10){
                val %= 10;
            }
            end.next = new ListNode(val);
            end = end.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        ListNode remain = l1 == null ? l2 : l1;
        while (remain != null){
            int val = remain.val + temp;
            temp = val / 10;
            if (val >= 10){
                val %= 10;
            }
            end.next = new ListNode(val);
            end = end.next;
            remain = remain.next;
        }
        if (temp > 0){
            end.next = new ListNode(temp);
        }
        return result.next;
    }
}
