package algorithm;

public class No287 {
    public int findDuplicate(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int low = 1, high = nums.length - 1, mid;
        while(low < high) {
            int count = 0;
            mid = low + (high - low) / 2;
            for (int i : nums) if (i <= mid) count++;
            if (count > mid) high = mid;
            else low = mid + 1;
        }
        return high;
    }
}
