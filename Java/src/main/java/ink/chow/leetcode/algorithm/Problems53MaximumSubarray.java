package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Problems53MaximumSubarray {

    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int pre = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int n = Math.max(pre + nums[i], nums[i]);
            max = Math.max(max, n);
            pre = n;
        }
        return max;
    }

}
