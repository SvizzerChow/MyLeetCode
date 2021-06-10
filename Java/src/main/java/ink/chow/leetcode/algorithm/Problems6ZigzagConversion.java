package ink.chow.leetcode.algorithm;

public class Problems6ZigzagConversion {

    public String convert(String s, int numRows) {
        if (s == null || s.length() <= 1 || numRows <= 1){
            return s;
        }
        char[] result = new char[s.length()];
        int index = 0;
        int hight = 0;
        int temp = 0;
        boolean d = true;
        while (hight < numRows && index < s.length()) {
            int i = d ? temp + hight : temp + numRows - hight - 1;
            if (((hight > 0 && hight < numRows -1) || d)) {
                if (i < s.length()) {
                    result[index++] = s.charAt(i);
                } else {
                    hight++;
                    temp = 0;
                    d = true;
                    continue;
                }
            }
            d = !d;
            temp += numRows -1;
        }
        return new String(result);
    }

    public static void main(String[] args) {
        System.out.println(new Problems6ZigzagConversion().convert("AB", 1));
    }
}
