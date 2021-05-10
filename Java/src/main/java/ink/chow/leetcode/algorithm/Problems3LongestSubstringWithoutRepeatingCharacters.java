package ink.chow.leetcode.algorithm;

import java.util.*;

public class Problems3LongestSubstringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        int start = 0, end = 0;
        Map<Character, Integer> index = new HashMap<>();
        while (start > end  || end < s.length()) {
            char c = s.charAt(end);
            if (index.containsKey(c)) {
                Integer temp = index.get(c);
                if (temp >= start){
                    maxLength = Math.max(maxLength, end - start);
                    start = temp + 1;
                }
            }
            index.put(c, end);
            end ++;
        }
        return Math.max(maxLength, end - start);
    }


    public static void main(String[] args) {
        Problems3LongestSubstringWithoutRepeatingCharacters p = new Problems3LongestSubstringWithoutRepeatingCharacters();
        System.out.println(p.lengthOfLongestSubstring("abcabcbb"));
    }


}
