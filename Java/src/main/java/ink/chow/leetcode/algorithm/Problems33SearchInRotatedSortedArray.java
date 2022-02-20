package ink.chow.leetcode.algorithm;



public class Problems33SearchInRotatedSortedArray {

    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int index = -1;
        if (nums[left] > nums[right]) {
            while (left < right) {
                int mid = (right + left) / 2;
                if (nums[mid] > nums[left]) {
                    left = mid;
                } else {
                    right = mid;
                }
            }
            index = left;
        }
        if (index >= 0 && target >= nums[0]) {
            return halfSearch(nums, target, 0, index);
        } else {
            return halfSearch(nums, target, index >= 0 ? index + 1 : 0, nums.length - 1);
        }
    }

    public int halfSearch(int[] nums, int target, int start, int end) {
        while (start < end) {
            if (nums[start] == target) {
                return start;
            } else if( nums[start] > target) {
                return -1;
            }
            int mid = (start + end) / 2;
            if (nums[mid] > target) {
                end = mid;
            } else if (nums[mid] < target){
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return start == end && nums[start] == target ? start : -1;
    }
    public static void main(String[] args) {
        System.out.println(new Problems33SearchInRotatedSortedArray().search(new int[]{1, 3}, 1));
    }
}
