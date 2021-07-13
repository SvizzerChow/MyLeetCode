package ink.chow.leetcode.algorithm;

import java.util.LinkedHashMap;
import java.util.Map;

public class Problems13RomanToInteger {
    private Map<String, Integer> map = new LinkedHashMap<>();
    {
        map.put("M", 1000);
        map.put("CM", 900);
        map.put("D", 500);
        map.put("CD", 400);
        map.put("C", 100);
        map.put("XC", 90);
        map.put("L", 50);
        map.put("XL", 40);
        map.put("X", 10);
        map.put("IX", 9);
        map.put("V", 5);
        map.put("IV", 4);
        map.put("I", 1);
    }
    public int romanToInt(String s) {
        int index = 0;
        int result = 0;
        if (s.length() < 1) {
            return 0;
        }
        while (index < s.length()) {
            char c = s.charAt(index);
            if ((c=='C' || c == 'X' || c == 'I') && index + 2 <= s.length()) {
                String cc = s.substring(index, index+2);
                if (map.containsKey(cc)) {
                    result += map.get(cc);
                    index += 2;
                    continue;
                }
            }
            result += map.get(String.valueOf(c));
            index += 1;
        }
        return result;
    }
}
