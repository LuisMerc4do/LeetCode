class Solution:
    def max_area(self, heights):
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height

            max_area = max(max_area, current_area)

            # Move the pointers inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
    
    
    
## EXPLANATION

class Solution:
    def max_area(self, heights):
        # Initialize two pointers: 'left' at the start and 'right' at the end of the heights list.
        left, right = 0, len(heights) - 1
        
        # Variable to keep track of the maximum area found so far.
        max_area = 0

        # Continue until the two pointers meet.
        while left < right:
            # Calculate the width of the current container (distance between left and right).
            width = right - left
            
            # Calculate the height of the container, which is the shorter of the two heights (heights[left] and heights[right]).
            height = min(heights[left], heights[right])
            
            # Calculate the current area using the formula: area = width * height.
            current_area = width * height
            
            # Update max_area if the current area is greater than the previously recorded maximum.
            max_area = max(max_area, current_area)

            # Move the pointers inward to try and find a larger container:
            # - If heights[left] is smaller, move the left pointer to the right to potentially find a taller container.
            # - If heights[right] is smaller or equal, move the right pointer to the left.
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # After the loop, return the maximum area found.
        return max_area
