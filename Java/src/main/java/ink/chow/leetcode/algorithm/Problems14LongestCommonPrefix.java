package ink.chow.leetcode.algorithm;

public class Problems14LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length <= 1) {
            return strs[0];
        }
        String result = strs[0];
        for (int i = 1; i < strs.length; i++) {
            result = commonPrefix(result, strs[i]);
            if (result.isBlank()) {
                break;
            }
        }
        return result;
    }

    private String commonPrefix(String one, String two) {
        int index = 0;
        StringBuilder stringBuilder = new StringBuilder();
        while (index < one.length() && index < two.length()) {
            if (one.charAt(index) != two.charAt(index)) {
                break;
            }
            stringBuilder.append(one.charAt(index));
            index ++;
        }
        return stringBuilder.toString();
    }
}
