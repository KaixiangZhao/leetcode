package algorithm;

public class No122 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) return 0;
        int result = 0;
        int a = prices[0];
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > a)
                result += prices[i] - a;
            a = prices[i];
        }
        return result;
    }
}
