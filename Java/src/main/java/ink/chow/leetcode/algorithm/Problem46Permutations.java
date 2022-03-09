package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Problem46Permutations {

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            temp.add(nums[i]);
        }
        backtrack(0, temp, result);
        return result;
    }


    private void backtrack(int index, List<Integer> temp, List<List<Integer>> result) {
        if (index == temp.size()) {
            result.add(new ArrayList<>(temp));
            return;
        }
        for (int i = index; i < temp.size(); i++) {
            Collections.swap(temp, index, i);
            backtrack(index+1, temp, result);
            Collections.swap(temp, i, index);
        }
    }

    public static void main(String[] args) {
        System.out.println(new Problem46Permutations().permute(new int[]{1, 2, 4, 5}));
    }
}
