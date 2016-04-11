package algorithm;

import datastructure.TreeNode;

public class No108 {
    public TreeNode sortedArrayToBST(int[] nums) {
        int low = 0, high = nums.length;
        return sortedArrayToBST(nums, low, high);
    }

    public TreeNode sortedArrayToBST(int[] nums, int low, int high) {
        TreeNode treeHead = null;
        if(low < high) {
            int mid = low + (high-low)/2;
            treeHead = new TreeNode(nums[mid]);
            treeHead.left = sortedArrayToBST(nums, low, mid);
            treeHead.right = sortedArrayToBST(nums, mid+1, high);
        }
        return treeHead;
    }
}
