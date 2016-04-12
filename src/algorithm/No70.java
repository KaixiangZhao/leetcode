package algorithm;

public class No70 {
    public int climbStairs(int n) {
        int pre = 0, curr = 1;
        while (n-- > 0) {
            curr = pre + curr;
            pre = curr - pre;
        }
        return curr;
    }
}
