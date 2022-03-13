package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Problems49GroupAnagrams {

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<String>> map = new HashMap<>();
        for (String str : strs) {
            int temp = 0;
            for (int i = 0; i < str.length(); i++) {
                temp += hash(str.charAt(i));
            }
            List<String> list = map.computeIfAbsent(temp, s -> new ArrayList<>());
            list.add(str);
        }
        return new ArrayList<>(map.values());
    }

    private int hash(int a) {
        return a*a*a*a;
    }


    public static void main(String[] args) {
        System.out.println(new Problems49GroupAnagrams().hash(23));
    }


}
