package algorithm;

import datastructure.TreeNode;

public class No230 {
    int count = 0;
    int result = Integer.MIN_VALUE;

    public int kthSmallest(TreeNode root, int k) {
        traverse(root, k);
        return result;
    }

    public void traverse(TreeNode root, int k) {
        if(root == null) return;
        traverse(root.left, k);
        if(++count == k) result = root.val;
        traverse(root.right, k);
    }
}
