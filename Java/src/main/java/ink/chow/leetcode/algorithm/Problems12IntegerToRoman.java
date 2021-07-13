package ink.chow.leetcode.algorithm;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class Problems12IntegerToRoman {
    private Map<Integer, String> map = new LinkedHashMap<>();
    {
        map.put(1000, "M");
        map.put(900, "CM");
        map.put(500, "D");
        map.put(400, "CD");
        map.put(100, "C");
        map.put(90, "XC");
        map.put(50, "L");
        map.put(40, "XL");
        map.put(10, "X");
        map.put(9, "IX");
        map.put(5, "V");
        map.put(4, "IV");
        map.put(1, "I");
    }

    public String intToRoman(int num) {
        StringBuilder stringBuffer = new StringBuilder();
        while (num > 0) {
            for (Integer i : map.keySet()) {
                if (num < i) {
                    continue;
                }
                int count = num / i;
                for (int j=0; j<count; j++) {
                    stringBuffer.append(map.get(i));
                }
                num = num % i;
            }
        }
        return stringBuffer.toString();
    }

    public static void main(String[] args) {
        System.out.println(new Problems12IntegerToRoman().intToRoman(1994));
    }
}
