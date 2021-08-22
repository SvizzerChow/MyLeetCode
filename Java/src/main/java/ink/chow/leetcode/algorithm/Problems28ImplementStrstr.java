package ink.chow.leetcode.algorithm;

public class Problems28ImplementStrstr {
    public int strStr(String haystack, String needle) {
        if (needle.isBlank()) {
            return 0;
        }
        int index = 0;
        while (index < haystack.length()) {
            if (haystack.charAt(index) == needle.charAt(0)
                    && index+needle.length()-1 < haystack.length()
                    && haystack.charAt(index+needle.length()-1) == needle.charAt(needle.length()-1)) {
                int temp = 0;
                while (temp < needle.length()) {
                    if (index+temp < haystack.length() && haystack.charAt(index+temp) == needle.charAt(temp)) {
                        temp ++;
                    } else {
                        break;
                    }
                }
                if (temp == needle.length()) {
                    return index;
                }
            }
            index ++;
        }
        return -1;
    }
}
