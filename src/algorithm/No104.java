package algorithm;

import datastructure.TreeNode;

public class No104 {

    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        else
            return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }

    public static void main(String[] args) {
        TreeNode a, b, c, d;
        a = new TreeNode(1);
        b = new TreeNode(2);
        c = new TreeNode(3);
        d = new TreeNode(4);
        a.right = b;
        b.right = c;
        c.right = d;
        No104 app = new No104();
        System.out.println(app.maxDepth(a));
    }
}
