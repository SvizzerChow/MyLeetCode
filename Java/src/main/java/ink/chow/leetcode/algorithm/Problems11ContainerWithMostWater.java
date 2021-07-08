package ink.chow.leetcode.algorithm;

public class Problems11ContainerWithMostWater {
    public int maxArea(int[] height) {
        if (height.length <= 1) {
            return 0;
        }
        int max = 0;
        int left = 0;
        int right = height.length -1;
        while (left < right) {
            int temp = Math.min(height[right] , height[left]);
            max = Math.max(temp * (right - left), max);
            if (height[left] <= height[right]) {
                left ++;
            }else {
                right --;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        System.out.println(new Problems11ContainerWithMostWater().maxArea(new int[]{1, 2, 3, 4, 2}));
    }
}
