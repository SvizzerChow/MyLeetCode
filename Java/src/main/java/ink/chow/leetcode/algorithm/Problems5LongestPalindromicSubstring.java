package ink.chow.leetcode.algorithm;

import java.util.HashMap;
import java.util.Map;

public class Problems5LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++){
            String temp = longestPalindrome(s, i);
            if (temp.length() > result.length()){
                result = temp;
            }
            temp = longestPalindrome(s, i, i+1);
            if (temp.length() > result.length()){
                result = temp;
            }
        }
        return result;
    }

    private String longestPalindrome(String s, int index){
        int left = index - 1;
        int right = index + 1;
        return longestPalindrome(s, left, right);
    }

    private String longestPalindrome(String s, int left, int right){
        while (left >= 0 && right < s.length()){
            if (s.charAt(left) != s.charAt(right)){
                break;
            }
            left --;
            right ++;
        }
        return s.substring(left +1, right);
    }

    public static void main(String[] args) {
        Problems5LongestPalindromicSubstring problems4LongestPalindromicSubstring = new Problems5LongestPalindromicSubstring();
        System.out.println(problems4LongestPalindromicSubstring.longestPalindrome("bb"));
    }
}
