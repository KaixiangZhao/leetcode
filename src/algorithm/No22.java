package algorithm;

import java.util.ArrayList;
import java.util.List;

public class No22 {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        helper(ans, n, 0, "");
        return ans;
    }

    public void helper(List<String> ans, int n, int limit, String s) {
        if (s.length() == 2 * n) {ans.add(s); return;}
        if (limit > 0 && s.length() - limit < limit) helper(ans, n, limit, s + ")");
        if (limit < n) helper(ans, n, limit + 1, s + "(");
    }
}
