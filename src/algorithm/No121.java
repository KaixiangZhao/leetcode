package algorithm;

public class No121 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) return 0;
        int result = 0;
        int a = 0;
        for (int i = 1; i < prices.length; i++) {
            a += prices[i] - prices[i - 1];
            if (a > result) result = a;
            if (a < 0) a = 0;
        }
        return result;
    }
}
