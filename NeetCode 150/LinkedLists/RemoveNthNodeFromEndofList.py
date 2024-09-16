class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        This method removes the nth node from the end of the list and returns the head of the modified list.
        """
        dummy = ListNode(0)
        dummy.next = head
        
        fast, slow = dummy, dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next