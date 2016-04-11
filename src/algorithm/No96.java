package algorithm;

public class No96 {
    public int numTrees(int n) {
        int[] num = new int[n + 1];
        return calculate(n, num);
    }

    public int calculate(int n, int[] num) {
        if (n == 0 || n == 1) return 1;
        int count = 0;
        for (int i = 0; i < n; i++) count += (num[i] == 0 ? calculate(i, num) : num[i]) * (num[n-1-i] == 0 ? calculate(n-1-i, num) : num[n-1-i]);
        if (num[n] == 0) num[n] = count;
        return count;
    }
}
