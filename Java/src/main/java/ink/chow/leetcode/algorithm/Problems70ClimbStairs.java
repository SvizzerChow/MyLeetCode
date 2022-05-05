package ink.chow.leetcode.algorithm;



public class Problems70ClimbStairs {

    public int climbStairs(int n) {
        int a = 1;
        int b = 1;
        for (int i = 2; i <= n; i ++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    public static void main(String[] args) {
        System.out.println(new Problems70ClimbStairs().climbStairs(3));
    }
}
