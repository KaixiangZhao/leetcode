from src.datastructure.TreeNode import TreeNode


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        result = []
        list = [[root]]
        index = 0
        while True:
            stack = []
            for node in list[index]:
                if node.left != None:
                    stack.append(node.left)
                if node.right != None:
                    stack.append(node.right)
            index += 1
            if stack == []:
                break
            else:
                list.append(stack)

        for i in range(index):
            result.append(list[i].pop().val)

        return result
