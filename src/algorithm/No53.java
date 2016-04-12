package algorithm;

public class No53 {
    public int maxSubArray(int[] nums) {
        int sum = nums[0];
        int maxSum = sum;
        for (int i = 1; i < nums.length; i++) {
            if (sum < 0) sum = 0;
            sum += nums[i];
            if (sum > maxSum) maxSum = sum;
        }
        return maxSum;
    }
}
