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