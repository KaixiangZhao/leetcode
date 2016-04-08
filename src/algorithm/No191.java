package algorithm;

public class No191 {
    public int hammingWeight(int n) {
        int sum=0;
        String[] x=Integer.toBinaryString(n).split("");
        for (String s : x) if (s.equals("1")) ++sum;
        return sum;
    }
}
