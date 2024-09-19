class Solution:
    def minHarvestRate(self, apples, h):
        def time_taken(rate):
            time = 0 
            for i in range(len(apples)):
                time += (apples[i] + rate - 1) // rate
            return time
        left, right = 0, len(apples) - 1
        while left < right:
            mid = (left - right) // 2
            if time_taken(mid) > h:
                left = mid + 1
            else:
                right = right + 1
        return left
    

#   EXPLANATION
class Solution:
    def minHarvestRate(self, apples, h):
        # Helper function to calculate time needed to harvest apples at a given rate
        def time_taken(rate):
            time = 0
            for i in range(len(apples)):
                # For each pile of apples, calculate how long it takes to harvest at the current rate
                # The formula `(apples[i] + rate - 1) // rate` gives the time taken for each pile
                time += (apples[i] + rate - 1) // rate
            return time
        # Set the initial range for the possible minimum harvest rate
        left, right = 1, max(apples)  # Harvest rate can range from 1 to the largest pile of apples        
        # Perform binary search to find the minimum rate
        while left < right:
            mid = (left + right) // 2  # Middle rate between left and right bounds         
            # Calculate the time it would take with the current middle rate
            if time_taken(mid) > h:
                # If the time exceeds the allowed hours, we need a higher rate, so adjust left boundary
                left = mid + 1
            else:
                # If the time is within the allowed hours, try a lower rate by adjusting right boundary
                right = mid   
        # Return the minimum rate found
        return left
