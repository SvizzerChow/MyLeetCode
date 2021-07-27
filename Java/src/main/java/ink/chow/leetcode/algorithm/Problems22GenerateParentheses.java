package ink.chow.leetcode.algorithm;


import java.util.ArrayList;
import java.util.List;

public class Problems22GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generateParenthesis(n, n, "",result);
        return result;
    }

    private void generateParenthesis(int left, int right, String str, List<String> result) {
        if (left == right && left == 0) {
            result.add(str);
            return;
        }
        if (left == right) {
            generateParenthesis(left - 1, right, str + '(', result);
            return;
        }
        if (left > 0) {
            generateParenthesis(left - 1, right, str + '(', result);
        }
        if (right > 0) {
            generateParenthesis(left, right - 1, str + ')', result);
        }
    }

    public static void main(String[] args) {
        System.out.println(new Problems22GenerateParentheses().generateParenthesis(2));
    }
}
