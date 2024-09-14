# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        # The value stored in the node
        self.val = x
        # The pointer to the next node in the list, initialized to None
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        This method checks if the given singly-linked list contains a cycle.
        """
        # Check if the list is empty. If it is, it can't have a cycle.
        if not head:
            return False
        # Initialize the current node as the head of the list
        current = head
        # Initialize a set to store nodes that we have already seen
        hasSeen = set()
        # Traverse the list until we either find a cycle or reach the end
        while current:
            # If the next node is None, the list has ended, so no cycle
            if current.next is None:
                return False
            # If the current node is already in the set, we have a cycle
            if current in hasSeen:
                break
            # Add the current node to the set to mark it as seen
            hasSeen.add(current)
            # Move to the next node in the list
            current = current.next
        # If we exit the loop by breaking, it means we found a cycle
        return True
