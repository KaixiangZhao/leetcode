package algorithm;

import datastructure.TreeLinkNode;

public class No116 {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        while (root.left != null) {
            TreeLinkNode tmp = root;
            while (tmp != null) {
                tmp.left.next = tmp.right;
                if (tmp.next != null) tmp.right.next = tmp.next.left;
                tmp = tmp.next;
            }
            root = root.left;
        }
    }
}
