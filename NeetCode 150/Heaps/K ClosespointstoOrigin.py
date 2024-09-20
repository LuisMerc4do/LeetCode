import heapq
import math  # Import the math module to use the square root function

def k_closest(points, k):
    # If the list of points is empty, return None
    if not points:
        return
    # Create an empty heap (max-heap using negative distances)
    heap = []
    # Iterate over all the points
    for x, y in points:
        # Calculate the Euclidean distance from the origin to the point (x, y)
        distance = math.sqrt(x**2 + y**2)
        # If the heap contains fewer than k points, add the current point and its negative distance
        # We use -distance to simulate a max-heap since Python's heapq is a min-heap by default
        if len(heap) < k:
            heapq.heappush(heap, (-distance, [x, y]))
        # If the heap already contains k points, compare the current point's distance with
        # the farthest point in the heap (which is the top of the max-heap with the smallest negative distance)
        # If the current point is closer than the farthest point, replace it
        else:
            heapq.heappushpop(heap, (-distance, [x, y]))
    # Return the k closest points from the heap, extracting only the coordinates from the tuples
    return [heap[i][1] for i in range(k)]
