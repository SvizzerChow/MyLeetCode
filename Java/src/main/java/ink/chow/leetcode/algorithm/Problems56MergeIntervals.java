package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Problems56MergeIntervals {

    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        int i = 1;
        List<int[]> result = new ArrayList<>(intervals.length);
        result.add(intervals[0]);
        while (i < intervals.length) {
            int before = result.get(result.size() - 1)[1];
            int[] temp = intervals[i];
            if (temp[0] > before) {
                result.add(temp);
            } else if (temp[1] > before) {
                result.get(result.size() - 1)[1] = temp[1];
            }
            i++;
        }
        int[][] r = new int[result.size()][2];
        return result.toArray(r);
    }

    public static void main(String[] args) {
        int[][] r = new Problems56MergeIntervals().merge(new int[][]{{1, 3}, {5, 8}, {2, 6}, {11, 15}, {22, 28}});
        Arrays.stream(r).forEach(s-> System.out.println(Arrays.toString(s)));

    }
}
