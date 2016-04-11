package algorithm;

public class No35 {
    public int searchInsert(int[] nums, int target) {
        int index = 0;
        while (index < nums.length){
            if (target > nums[index]) { index++; continue; }
            return index;
        }
        return index;
    }
}
