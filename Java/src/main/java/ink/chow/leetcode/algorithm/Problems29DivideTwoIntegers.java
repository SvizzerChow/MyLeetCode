package ink.chow.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Problems29DivideTwoIntegers {
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
            return 0;
        }
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        if (divisor == 1 ) {
            return dividend;
        }
        if (divisor == -1) {
            return -dividend;
        }
        boolean flag = (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0);
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;
        if (dividend > divisor) {
            return 0;
        }
        int count;
        int temp = divisor;
        List<Integer> list = new ArrayList<>();
        int p = 1;
        while (dividend < temp) {
            if (dividend - temp > temp) {
                break;
            }
            list.add(temp);
            temp += temp;
            p += p;
        }
        dividend -= temp;
        count = (flag ? p : -p);
        for (int i = list.size() -1; i >= 0; i--) {
            Integer t = list.get(i);
            p /= 2;
            if (t < dividend) {
                continue;
            }
            dividend -= t;
            count = count + (flag ? p : -p);
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(new Problems29DivideTwoIntegers().divide(2147483647, 2));
    }
}
