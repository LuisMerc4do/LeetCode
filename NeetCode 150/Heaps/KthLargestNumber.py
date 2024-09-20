import heapq  # Import the heapq library, which provides heap (priority queue) functionality

def kth_largestNumber(nums, k):
    if not nums:
        return
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappush(heap, num)
    return heap[0]














def kth_largest(nums, k):
    # If the list is empty, return None
    if not nums:
        return 
    # Create an empty heap (which will be used as a min-heap)
    heap = []
    # Iterate over the elements in the nums list
    for num in nums:
        # If the heap size is less than k, add the current number to the heap
        if len(heap) < k:
            heapq.heappush(heap, num)
        # If the current number is larger than the smallest element in the heap (heap[0]),
        # pop the smallest element and add the current number to the heap.
        # This ensures that the heap only holds the largest k elements.
        elif num > heap[0]:
            heapq.heappushpop(heap, num)
    # After the loop, heap[0] will be the k-th largest element, because we are maintaining
    # the k largest elements in the heap and the smallest of those k elements will be at the top.
    return heap[0]
