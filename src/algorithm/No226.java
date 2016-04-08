package algorithm;

import datastructure.TreeNode;

public class No226 {
    public TreeNode invertTree(TreeNode root) {
        TreeNode tmp;
        if (root == null)
            return null;
        else {
            tmp = root.left;
            root.left = invertTree(root.right);
            root.right = invertTree(tmp);
            return root;
        }

    }
}
