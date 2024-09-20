import heapq
def k_closest(nums, k, target):
    heap = []
    for num in nums:
        distance = abs(nums - target)
        if len(heap) < k:
            heapq.heappush(heap, (-distance, num))
        elif distance < -heap[0][0]:
            heapq.heappushpop(heap, (-distance, num))
    
    distances = [pair[1] for pair in heap]
    distances.sort()
    return distances