package ink.chow.leetcode.algorithm;


public class Problems9PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x < 10) {
            return true;
        }
        if (x % 10 == 0){
            return false;
        }
        int r = 0;
        while (x > 0) {
            int temp = x % 10;
            x = x / 10;
            if (x > 0 && r == x) {
                return true;
            }
            r = r*10 + temp;
            if (r == x) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(new Problems9PalindromeNumber().isPalindrome(1110));
    }
}
