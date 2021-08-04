package ink.chow.leetcode.algorithm;

import java.util.Arrays;

public class Problems27RemoveElement {
    public int removeElement(int[] nums, int val) {
        int length = nums.length;
        int index = 0;
        boolean flag = false;
        int preIndex = -1;
        while (index < nums.length) {
            if (nums[index] == val) {
                flag = true;
                length --;
            } else {
                preIndex ++;
                if (flag) {
                    nums[preIndex] = nums[index];
                }
            }
            index ++;
        }
        return length;
    }


    public static void main(String[] args) {
        int[] data = new int[]{1, 2, 3, 3, 4};
        System.out.println(new Problems27RemoveElement().removeElement(data, 3));
        System.out.println(Arrays.toString(data));
    }
}
