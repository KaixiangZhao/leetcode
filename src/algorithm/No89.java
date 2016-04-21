package algorithm;

import java.util.ArrayList;
import java.util.List;

public class No89 {
    public List<Integer> grayCode(int n) {
        int count = (int)Math.pow(2,n);
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < count; i++) res.add((i) ^ (i >> 1));
        return res;
    }
}
