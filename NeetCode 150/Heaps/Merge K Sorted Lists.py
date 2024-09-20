import heapq
def mergeKLists(lists):
    if not lists:
        return None
    heap = []
    for index, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, index, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, index, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
    
        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))
    return dummy.next


# EXPLANATION

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # If the list of linked lists is empty, return None
    if not lists:
        return None
    
    # Create an empty heap (min-heap)
    heap = []
    
    # Push the first node of each linked list into the heap.
    # We push a tuple of (node value, index of list, node) into the heap to maintain sorting.
    for index, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, index, node))
    
    # Create a dummy node to easily return the merged list later.
    dummy = ListNode(0)
    curr = dummy  # Pointer to keep track of the current node in the merged list.
    
    # Process the heap until it's empty.
    while heap:
        # Pop the smallest node from the heap.
        val, index, node = heapq.heappop(heap)
        
        # Append this node to the merged list.
        curr.next = node
        curr = curr.next  # Move the current pointer to the next position.
    
        # If the node has a next node, push it into the heap.
        if node.next:
            heapq.heappush(heap, (node.next.val, index, node.next))
    
    # Return the next node after the dummy, which is the head of the merged list.
    return dummy.next
