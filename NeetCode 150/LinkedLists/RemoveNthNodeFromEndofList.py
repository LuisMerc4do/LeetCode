class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        This method removes the nth node from the end of the list and returns the head of the modified list.
        """
        # Create a dummy node that points to the head of the list
        # This helps to simplify edge cases, such as removing the head of the list
        dummy = ListNode(0, head)
        # Initialize two pointers: left starts at the dummy node, and right starts at the head
        left = dummy
        right = head
        # Move the right pointer `n` steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
        # Move both pointers until the right pointer reaches the end of the list
        # After this loop, left will be pointing to the node right before the one we want to remove
        while right:
            left = left.next
            right = right.next
        # Skip the node that needs to be removed
        left.next = left.next.next
        # Return the head of the modified list, which is the next node after dummy
        return dummy.next