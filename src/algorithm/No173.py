from src.datastructure.TreeNode import TreeNode


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = self.push_all_nodes(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []


    def next(self):
        """
        :rtype: int
        """
        min = self.stack.pop()
        self.stack.extend(self.push_all_nodes(min.right))
        return min.val


    def push_all_nodes(self, node):
        stack = []
        while node != None:
            stack.append(node)
            node = node.left
        return stack


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())