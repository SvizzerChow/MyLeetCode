package ink.chow.leetcode.algorithm;


import java.util.Arrays;

public class Problems34FindFirstLastPositionElementInSortedArray {

    public int[] searchRange(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int[] result = new int[]{-1, -1};
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > target) {
                right = mid;
            }
            else if (nums[mid] == target) {
                left = mid + 1;
            } else {
                left = mid + 1;
            }
        }
        if (left == right && nums[left] == target) {
            result[1] = left;
        } else if (left == right && left > 0 && nums[left - 1] == target) {
            result[1] = left - 1;
        }

        left = 0;
        right = nums.length - 1;
        while (left < right) {
            int mid = (left + right) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            }
            else if (nums[mid] == target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        if (left == right && nums[left] == target) {
            result[0] = left;
            if (result[1] == -1) {
                result[1] = left;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Problems34FindFirstLastPositionElementInSortedArray().searchRange(new int[]{1}, 3)));
    }
}
