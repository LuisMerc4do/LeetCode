class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        counter = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                counter += 1
        return len(intervals) - counter