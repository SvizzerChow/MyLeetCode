package ink.chow.leetcode.algorithm;

public class Problems7ReverseInteger {
    public int reverse(int x) {
        boolean flag = x > 0;
        int result = 0;
        x = Math.abs(x);
        while (x > 0) {
            int temp = x % 10;
            System.out.println("\n2147483647");
            System.out.println(result);
            System.out.println((long) result * 10 + temp);
            if ((result > Integer.MAX_VALUE/10) || (result == Integer.MAX_VALUE/10 && temp >= 7)) {
                return 0;
            }
            result = result * 10 + temp;
            x = x / 10;
        }
        return flag ? result : -result;
    }

    public static void main(String[] args) {
        System.out.println(new Problems7ReverseInteger().reverse(1563847412));
    }
}
