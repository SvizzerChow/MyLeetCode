package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class Problems39CombinationSum {

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List list = combinationSum(candidates, target, 0);
        return list;
    }

    private List<List<Integer>> combinationSum(int[] candidates, int target, int index) {
        List<List<Integer>> result = new ArrayList<>();
        for (int i=index; i < candidates.length; i++) {
            if (target == candidates[i]) {
                ArrayList<Integer> l = new ArrayList<>();
                l.add(target);
                result.add(l);
            } else if (target > candidates[i]) {
                int finalI = i;
                result.addAll(combinationSum(candidates, target - candidates[i], i)
                        .stream()
                                .peek(s -> s.add(candidates[finalI]))
                        .collect(Collectors.toList()));
            } else {
                break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Problems39CombinationSum().combinationSum(new int[]{1, 2, 4, 5, 7}, 7));
    }
}
