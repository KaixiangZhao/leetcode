package algorithm;

import datastructure.TreeNode;

public class No100 {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //if (p == null && q == null) return true;
        //if (p == null || q == null) return false;
        //return p.val == q.val && isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
        return((p == null || q == null)?(p==q):(p.val==q.val && isSameTree(p.right, q.right) && isSameTree(p.left, q.left)));
    }
}
