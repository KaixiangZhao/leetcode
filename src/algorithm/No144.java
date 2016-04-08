package algorithm;

import datastructure.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class No144 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if (root == null) return list;
        list.add(root.val);
        preorder(root.left, list);
        preorder(root.right, list);
        return list;
    }

    public void preorder(TreeNode root, List<Integer> list) {
        if (root == null) return;
        list.add(root.val);
        preorder(root.left, list);
        preorder(root.right, list);
    }
}
