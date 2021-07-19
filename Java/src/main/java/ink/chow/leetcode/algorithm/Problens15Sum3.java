package ink.chow.leetcode.algorithm;

import java.util.*;

public class Problens15Sum3 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        if (nums.length < 3) {
            return new ArrayList<>();
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int idx=0; idx < nums.length; idx++) {
            map.put(nums[idx], idx);
        }
        int start = 0;
        List<List<Integer>> result = new ArrayList<>();
        while (start < nums.length - 2) {
            int nStart = nums[start];
            int mid = start + 1;
            while (mid < nums.length - 1) {
                int nMid = nums[mid];
                Integer end = map.get(-(nMid+nStart));
                if (end != null && end > mid) {
                    result.add(Arrays.asList(nStart, nMid, -(nMid + nStart)));
                }
                mid = map.get(nMid) + 1;
            }
            start = map.get(nStart) + 1;
        }
         return result;
    }

    public static void main(String[] args) {
        System.out.println(new Problens15Sum3().threeSum(new int[ ]{-1,0,1,2,-1,-4}));
    }
}
