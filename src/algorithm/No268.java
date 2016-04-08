package algorithm;

public class No268 {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int tmp;
        for (int i = 0; i < n; i++)
            if (nums[i] != i)
                if (nums[i] != n) {
                    tmp = nums[nums[i]];
                    nums[nums[i]] = nums[i];
                    nums[i] = tmp;
                    i--;
                }
        for (int i = 0; i < n; i++) if (nums[i] != i) return i;
        return n;
    }
}
