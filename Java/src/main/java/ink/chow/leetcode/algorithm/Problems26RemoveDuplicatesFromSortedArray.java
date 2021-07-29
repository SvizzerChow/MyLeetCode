package ink.chow.leetcode.algorithm;

import java.util.Arrays;

public class Problems26RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        int length = nums.length;
        int pre = nums[0];
        int preIndex = 0;
        boolean flag = false;
        for (int i=1; i<nums.length; i ++) {
            int temp = nums[i];
            if (temp > pre) {
                preIndex ++;
                pre = temp;
                if (flag) {
                    nums[preIndex] = temp;
                }
                continue;
            }
            length --;
            flag = true;
        }
        return length;
    }

    public static void main(String[] args) {
        int[] data = new int[]{1, 1, 2, 3, 5};
        System.out.println(new Problems26RemoveDuplicatesFromSortedArray().removeDuplicates(data));
        System.out.println(Arrays.toString(data));
    }
}
