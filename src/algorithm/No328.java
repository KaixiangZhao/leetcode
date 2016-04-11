package algorithm;

import datastructure.ListNode;

public class No328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return head;
        ListNode evenHead = head.next, evenPtr = head.next;
        ListNode oddPtr = head;
        while (evenPtr != null && evenPtr.next != null) {
            oddPtr.next = evenPtr.next;
            oddPtr = oddPtr.next;
            evenPtr.next = oddPtr.next;
            evenPtr = evenPtr.next;
        }
        oddPtr.next = evenHead;
        return head;
    }
}
