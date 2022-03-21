package ink.chow.leetcode.algorithm;


public class Problems55JumpGame {

    public boolean canJump(int[] nums) {
        int[] result = new int[nums.length];
        result[0] = nums[0] ;
        int i = 1;
        while (i < nums.length) {
            if (result[i - 1] <= 0) {
                return false;
            }
            result[i] = Math.max(result[i - 1] - 1, nums[i]);
            i++;
        }
        return result[result.length - 1] >= 0 || (result.length == 1 && result[0] == 0);
    }

    public static void main(String[] args) {
        System.out.println(new Problems55JumpGame().canJump(new int[]{2,0, 0}));
    }
}
