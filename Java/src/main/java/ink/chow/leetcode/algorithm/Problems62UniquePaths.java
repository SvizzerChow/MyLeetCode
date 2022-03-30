package ink.chow.leetcode.algorithm;

public class Problems62UniquePaths {

    public int uniquePaths(int m, int n) {
        int[][] result = new int[m][n];
        result[0][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j=0; j < n; j++) {
                int left = 0;
                int top = 0;
                if (i == 0 && j ==0) {
                    continue;
                }
                if (j > 0) {
                    left = result[i][j-1];
                }
                if (i > 0) {
                    top = result[i-1][j];
                }
                result[i][j] = left + top;
            }
        }
        return result[m-1][n-1];
    }
}
