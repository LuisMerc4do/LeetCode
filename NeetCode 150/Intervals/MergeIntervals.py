def mergeIntervals(intervals):
    sortedIntervals = intervals.sort(key=lambda x:x[0])
    merged = []
    
    for intervals in sortedIntervals:
        if not merged or intervals[0] > merged[-1][1]:
            merged.append(intervals)
        else:
            merged[-1][1] = max(merged[-1][1], intervals[1])
    return merged
        


## EXPLANATION

def mergeIntervals(intervals):
    # Sort the intervals based on the starting time (first element of each interval).
    sortedIntervals = intervals.sort(key=lambda x: x[0])  # Sort in-place.
    # Initialize an empty list to store merged intervals.
    merged = []
    # Iterate over each interval in the sorted list.
    for interval in intervals:  # `sortedIntervals` is None because `sort()` modifies in-place.
        # If the 'merged' list is empty or the current interval does not overlap with the last merged interval.
        if not merged or interval[0] > merged[-1][1]:
            # Append the current interval to the merged list.
            merged.append(interval)
        else:
            # There is overlap, so merge the intervals by updating the end of the last merged interval.
            merged[-1][1] = max(merged[-1][1], interval[1])
    # Return the list of merged intervals.
    return merged
