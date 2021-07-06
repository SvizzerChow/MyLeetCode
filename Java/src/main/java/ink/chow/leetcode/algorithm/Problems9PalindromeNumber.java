package ink.chow.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;

public class Problems9PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        List<Integer> list = new ArrayList<>();
        while (x > 0) {
            list.add(x % 10);
            x = x / 10;
        }
        if (list.size() <= 1) {
            return true;
        }
        int left = list.size()/2 - 1;
        int right = list.size() % 2 ==0 ? left + 1 : left + 2;
        while (left >= 0 && right < list.size()) {
            if (!list.get(left).equals(list.get(right))) {
                return false;
            }
            left --;
            right ++;
        }
        return true;
    }
}
