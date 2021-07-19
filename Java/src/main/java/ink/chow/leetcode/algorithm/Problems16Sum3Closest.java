package ink.chow.leetcode.algorithm;

import java.util.Arrays;

public class Problems16Sum3Closest {
    public int threeSumClosest(int[] nums, int target) {
        if (nums.length < 3) {
            return 0;
        }
        Arrays.sort(nums);
        int bast = 3 * (int)Math.pow(10, 4);
        for (int i = 0; i < nums.length - 2; i++) {
            int value = nums[i];
            int left = i+1, right = nums.length-1;
            int temp = target - value;
            while (left < right) {
                int a = nums[left] + nums[right];
                if (temp == a) {
                    return target;
                }
                if (Math.abs(bast - target) > Math.abs(a - temp)) {
                    bast = value + a;
                }
                if (temp > a) {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }
        return bast;
    }

    public static void main(String[] args) {
        System.out.println(new Problems16Sum3Closest().threeSumClosest(new int[]{-1,2,1,-4}, 1));
    }
}
