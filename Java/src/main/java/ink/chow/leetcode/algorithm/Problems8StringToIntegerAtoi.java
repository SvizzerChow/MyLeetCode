package ink.chow.leetcode.algorithm;

public class Problems8StringToIntegerAtoi {
    public int myAtoi(String s) {
        if (s.isBlank()) {
            return 0;
        }
        boolean flag = true;
        int index = 0;
        long result = 0;
        while (index < s.length()) {
            char p = s.charAt(index);
            index ++;
            if (p == ' ') {
                continue;
            }
            if (p == '-') {
                flag = false;
                break;
            }
            if (p == '+') {
                break;
            }
            int pp = p - '0';
            if (pp >=0 && pp <= 9) {
                index --;
                break;
            }
            return 0;
        }
        while (index < s.length()) {
            int p = s.charAt(index) - '0';
            if (p >=0 && p <= 9) {
                result = result*10 + p;
                if (result > Integer.MAX_VALUE) {
                    break;
                }
                index ++;
                continue;
            }
            break;
        }
        if (flag) {
            return result > Integer.MAX_VALUE? Integer.MAX_VALUE : (int)result;
        } else if (result >= Math.pow(2, 31)) {
            return (int)-Math.pow(2, 31);
        } else {
            return -(int)result;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Problems8StringToIntegerAtoi().myAtoi("-91283472332"));
        System.out.println((long)Math.pow(2, 31));
        System.out.println(Integer.MIN_VALUE);
    }
}
