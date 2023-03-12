package ink.chow.leetcode.algorithm;


import java.util.Arrays;

public class Problems75SortColors {

    public void sortColors(int[] nums) {
        int zero = 0, one = 0;
        int index = 0;
        if (nums.length <= 1) {
            return;
        }
        while (index < nums.length) {
            if (nums[index] == 0) {
                if (zero < one && one < index) {
                    int temp = nums[zero];
                    nums[zero] = nums[index];
                    int temp1 = nums[one];
                    nums[one] = temp;
                    nums[index] = temp1;
                } else {
                    int temp = nums[zero];
                    nums[zero] = nums[index];
                    nums[index] = temp;
                }
                one += 1;
                zero += 1;
            } else if (nums[index] == 1) {
                int temp = nums[one];
                nums[one] = nums[index];
                nums[index] = temp;
                one += 1;
            }
            index ++;
        }
    }


    public static void main(String[] args) {
        int[] data = new int[]{1, 0};
        new Problems75SortColors().sortColors(data);
        System.out.println(Arrays.toString(data));
    }
}
