package ink.chow.leetcode.algorithm;



public class Problems64MinimumPathSum {

    public int minPathSum(int[][] grid) {
        for (int i = 0; i < grid.length; i++) {
            for (int j=0; j<grid[i].length; j++) {
                if ( i==0 && j==0) {
                    continue;
                }
                int top = Integer.MAX_VALUE, left = Integer.MAX_VALUE;
                if (i > 0) {
                    top = grid[i-1][j];
                }
                if (j > 0) {
                    left = grid[i][j-1];
                }
                grid[i][j] += Math.min(top, left);
            }
        }
        return grid[grid.length-1][grid[0].length-1];
    }

    public static void main(String[] args) {
        System.out.println();
    }
}
