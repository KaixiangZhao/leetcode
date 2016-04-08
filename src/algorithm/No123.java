package algorithm;

public class No123 {
    public int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) return 0;
        int[] left = new int[prices.length];
        int[] right = new int[prices.length];
        int min = prices[0];
        for (int i = 1; i < prices.length; i++) {
            min = Math.min(min, prices[i]);
            left[i] = Math.max(left[i - 1], prices[i] - min);
        }
        int max = prices[prices.length - 1];
        for (int i = prices.length - 2; i >= 0; i--) {
            max = Math.max(max, prices[i]);
            right[i] = Math.max(right[i + 1], max - prices[i]);
        }
        int profit = Integer.MIN_VALUE;
        for (int i = 0; i < prices.length; i++) profit = Math.max(left[i] + right[i], profit);
        return profit;
    }

    public static void main(String[] args) {
        No123 app = new No123();
        int[] prices = {4,5,7,43,-24,16,32};
        int profit = app.maxProfit(prices);
    }
}
