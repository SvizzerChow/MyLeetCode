package ink.chow.leetcode.algorithm;

import java.util.*;

public class Problems17LetterCombinationsOfAPhoneNumber {
    private Map<Character, List<String>> map = new HashMap<>();
    {
        map.put('2', Arrays.asList("a", "b", "c"));
        map.put('3', Arrays.asList("d", "e", "f"));
        map.put('4', Arrays.asList("g", "h", "i"));
        map.put('5', Arrays.asList("j", "k", "l"));
        map.put('6', Arrays.asList("m", "n", "o"));
        map.put('7', Arrays.asList("p", "q", "r", "s"));
        map.put('8', Arrays.asList("t", "u", "v"));
        map.put('9', Arrays.asList("w", "x", "y", "z"));
    }
    public List<String> letterCombinations(String digits) {
        if (digits.length() < 1) {
            return Collections.emptyList();
        }
        List<String> list = new ArrayList<>(map.get(digits.charAt(0)));
        for (int i =1; i < digits.length(); i++) {
            List<String> temp = new ArrayList<>();
            for (String str : list) {
                for (String s : map.get(digits.charAt(i))) {
                    temp.add(str+s);
                }
            }
            list = temp;
        }
        return list;
    }

    public static void main(String[] args) {
        System.out.println(new Problems17LetterCombinationsOfAPhoneNumber().letterCombinations("23"));
    }
}
