package ink.chow.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Problems78SubSets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>());
        for (int i : nums) {
            int size = result.size();
            for (int j = 0; j < size; j++) {
                List<Integer> temp = new ArrayList<>(result.get(j));
                temp.add(i);
                result.add(temp);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Problems78SubSets().subsets(new int[]{1, 2, 3}));
    }
}
