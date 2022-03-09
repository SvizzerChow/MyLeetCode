package ink.chow.leetcode.algorithm;



public class Problems48RotateImage {

    public void rotate(int[][] matrix) {
        for (int j = 0; j < matrix.length/2; j++) {
            for (int i = j; i < matrix.length - 1 - j; i++) {
                trackback(matrix, i, j);
            }
        }
    }

    private void trackback(int[][] matrix, int x, int y) {
        int temp = matrix[y][x];
        System.out.println(temp);
        if (temp == 10001) {
            return;
        }
        matrix[y][x] = 10001;
        trackback(matrix,matrix.length - y - 1, x);
        matrix[x][matrix.length - y - 1] = temp;
    }
}
