from src.datastructure.ListNode import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        head = tmp
        head1, head2 = ListNode(0), ListNode(0)
        head1.next, head2.next = l1, l2
        while head1.next != None and head2.next != None:
            if head1.next.val < head2.next.val:
                tmp.next = head1.next
                tmp = tmp.next
                head1.next = head1.next.next
            else:
                tmp.next = head2.next
                tmp = tmp.next
                head2.next = head2.next.next
        if head1.next == None:
            tmp.next = head2.next
        else:
            tmp.next = head1.next
        return head.next