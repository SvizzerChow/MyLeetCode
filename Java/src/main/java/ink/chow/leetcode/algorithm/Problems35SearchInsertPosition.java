package ink.chow.leetcode.algorithm;


import java.util.Arrays;

public class Problems35SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] > target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[left] < target ? left + 1 : right;
    }

    public static void main(String[] args) {
        System.out.println(new Problems35SearchInsertPosition().searchInsert(new int[]{1, 2, 4, 5, 7}, 3));
    }
}
