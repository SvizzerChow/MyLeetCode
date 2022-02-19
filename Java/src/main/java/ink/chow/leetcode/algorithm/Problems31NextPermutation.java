package ink.chow.leetcode.algorithm;

import java.util.Arrays;

public class Problems31NextPermutation {

    public void nextPermutation(int[] nums) {
        int minIndex = -1;
        int index = nums.length - 2;
        while (index >= 0) {
            if (nums[index] < nums[index + 1]) {
                minIndex = index;
                break;
            }
            index--;
        }
        if (minIndex >= 0) {
            int lessIndex = -1;
            index = nums.length - 1;
            while (index > minIndex) {
                if (nums[index] > nums[minIndex]) {
                    lessIndex = index;
                    break;
                }
                index--;
            }
            // 交换
            int temp = nums[minIndex];
            nums[minIndex] = nums[lessIndex];
            nums[lessIndex] = temp;
        }
        index = minIndex + 1;
        int mid = (nums.length + index) / 2;
        int i = 0;
        while ((index + i) < mid) {
            int temp = nums[index + i];
            nums[index + i] = nums[nums.length - 1 - i];
            nums[nums.length - 1 - i] = temp;
            i++;
        }
    }

    public static void main(String[] args) {
        int[] data = new int[]{1, 3, 2};
        new Problems31NextPermutation().nextPermutation(data);
        System.out.println(Arrays.toString(data));
    }
}
