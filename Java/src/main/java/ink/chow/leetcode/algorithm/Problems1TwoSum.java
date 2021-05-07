package ink.chow.leetcode.algorithm;

import java.util.*;

public class Problems1TwoSum {

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[0];
        if (nums == null || nums.length == 0){
            return result;
        }
        if (nums.length == 1 && target != nums[0]){
            return result;
        }
        Map<Integer, Integer> cache = new HashMap<>();
        for (int i =0; i < nums.length; i++){
            if (cache.containsKey(target - nums[i])){
                return new int[]{cache.get(target - nums[i]), i};
            }
            cache.put(nums[i], i);
        }
        return result;
    }

    public static void main(String[] args) {
        int[] data = new int[]{3, 3};
        System.out.println(Arrays.toString(new Problems1TwoSum().twoSum(data, 7)));
    }
}
