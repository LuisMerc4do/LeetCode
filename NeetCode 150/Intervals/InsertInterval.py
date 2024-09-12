class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        merged = []
        sizeArr = len(intervals)
        counter = 0

        while counter < sizeArr and intervals[counter][1] < newInterval[0]:
            merged.append(intervals[counter])
            counter += 1
        while counter < sizeArr and intervals[counter][0] <= newInterval[1]:
            newInterval[0] = min(intervals[counter][0], newInterval[0])
            newInterval[1] = max(intervals[counter][1], newInterval[1])
            counter += 1
        
        merged.append(newInterval)
        for j in range(counter, sizeArr):
            merged.append(intervals[j])
        return merged