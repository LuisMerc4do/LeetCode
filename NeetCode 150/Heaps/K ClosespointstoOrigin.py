import heapq
class Solution:
    def kClosest(points: list[list[int]], k: int):
        if not points:
            return
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            distance = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-distance, i))
            elif distance < -heap[0][0]:
                heapq.heappushpop(heap, (-distance,1))
        return [points[p[1]] for p in heap]
    
    kClosest([[1,2],[2,3],[4,6],[5,1]], 3)