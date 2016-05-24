from src.datastructure.ListNode import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fnext, fnnext = head.next, head.next.next
        head.next = self.swapPairs(fnnext)
        fnext.next = head
        return fnext
