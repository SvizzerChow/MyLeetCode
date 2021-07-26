package ink.chow.leetcode.algorithm;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Problems20ValidParentheses {
    private final Map<Character, Character> MAP = Map.of(')', '(', '}', '{', ']', '[');
    public boolean isValid(String s) {
        if (s.length() <= 1 || s.length() % 2 == 1) {
            return false;
        }
        List<Character> list = new ArrayList<>(s.length());
        char c = s.charAt(0);
        list.add(c);
        for (int i = 1; i < s.length(); i++) {
            c = s.charAt(i);
            Character cc = MAP.get(c);
            if (cc != null) {
                if (list.size() == 0 || cc != list.get(list.size() - 1)) {
                    return false;
                }
                list.remove(list.size() - 1);
            } else {
                list.add(c);
            }
        }
        return list.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println(new Problems20ValidParentheses().isValid("{}"));
    }
}
