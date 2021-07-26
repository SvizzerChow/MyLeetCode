package ink.chow.leetcode.algorithm;

import java.util.*;
import java.util.stream.Collectors;

public class Problems18Sum4 {
    public List<List<Integer>> fourSum(final int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        Map<Integer, Integer> map = new HashMap<>();
        for (int j=0;j<nums.length;j++) {
            map.put(nums[j], j);
        }
        int i = 0;
        while (i < nums.length - 3) {
            List<List<Integer>> temp = threeSum(nums, target - nums[i], i+1, map);
            if (temp.size() > 0) {
                System.out.println(nums[i]+" " +temp);
                final int j = i;
                result.addAll(temp.stream()
                        .peek(s-> s.add(nums[j]))
                        .collect(Collectors.toList()));
            }
            i = map.get(nums[i]) + 1;
        }
        return result;
    }

    private List<List<Integer>> threeSum(int[] nums, int target, int start, Map<Integer, Integer> map) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int i = start;
        while (i < nums.length - 2) {
            int v = nums[i];
            int t = target - v;
            int left = i+1, right = nums.length -1;
            while (left < right) {
                int sum = nums[left] + nums[right];
                if (sum == t) {
                    result.add(new ArrayList<>(Arrays.asList(v, nums[left] , nums[right])));
                    left = map.get(nums[left]) + 1;
                } else if (sum > t) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
            i = map.get(v) + 1;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Problems18Sum4().fourSum(new int[]{-2,-1,-1,1,1,2,2}, 0));
    }
}
