from src.datastructure.TreeNode import TreeNode


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp != None:
                result.append(tmp.val)
                stack.append(tmp.left)
                stack.append(tmp.right)
        result.reverse()

        return result