package algorithm;

public class No309 {
    public int maxProfit(int[] prices) {
        if(prices.length <= 1)
            return 0;
        int[] c = new int[prices.length];
        int[] s = new int[prices.length];
        c[0] = 0;
        c[1] = 0;
        s[1] = prices[1] - prices[0];
        for(int i = 2; i < prices.length; i++){
            c[i] = Math.max(s[i-1], c[i-1]);
            s[i] = prices[i] - prices[i-1] + Math.max(c[i-2], s[i-1]);
        }
        return Math.max(c[prices.length-1], s[prices.length-1]);
    }
}
