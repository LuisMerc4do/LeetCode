class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # This holds the value for the node (like a number in the list)
        self.next = next  # This points to the next node in the list

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If there's no node or just one node, nothing to swap, so return the list as it is
        if not head or not head.next:
            return head
        # Create a pretend node to help make things easier to manage
        dummy = ListNode(0)
        dummy.next = head  # Point the pretend node to the start of the list
        # Use 'tail' to keep track of the end of the swapped part, and 'curr' to go through the list
        tail = dummy
        curr = head
        # Loop through the list, as long as there are at least two nodes left to swap
        while curr and curr.next:
            # Save the node that comes after the next pair (we'll need to reconnect it later)
            temp = curr.next.next
            # Swap the two nodes:
            # - The first node of the pair should now point to the second node of the pair
            tail.next = curr.next
            # - The second node of the pair should point back to the first node
            curr.next.next = curr
            # Now reconnect the first node to the part of the list we saved in 'temp'
            curr.next = temp
            # Move the 'tail' pointer to the first node in the pair, as it's now the last swapped node
            tail = curr
            # Move 'curr' to the next part of the list, so we can swap the next pair
            curr = temp
        # Return the new list, which starts right after the dummy node
        return dummy.next
