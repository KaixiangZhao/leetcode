package algorithm;

public class No326 {
    public boolean isPowerOfThree(int n) {
        return n > 0 && n == Math.pow(3, (int)(Math.log10(n) / Math.log10(3)));
    }
}
