package algorithm;

import java.util.ArrayList;
import java.util.List;

public class No202 {
    public boolean isHappy(int n) {
        List<Integer> cache = new ArrayList<>();
        int sumOfDigits = 0;
        while (true) {
            sumOfDigits += (n % 10) * (n % 10);
            n /= 10;
            if (n == 0) {
                if (cache.contains(sumOfDigits)) return false;
                else if (sumOfDigits == 1) return true;
                cache.add(sumOfDigits);
                n = sumOfDigits;
                sumOfDigits = 0;
            }
        }
    }
}
