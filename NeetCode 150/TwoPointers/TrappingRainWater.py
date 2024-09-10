def trappingWater(heights):
    left, right = 0, len(heights) - 1
    leftMax, rightMax = heights[left], heights[right]
    count = 0

    while left + 1 < right:
        if rightMax > leftMax:
            left += 1
            if heights[left] > leftMax:
                leftMax = heights[left]
            else:
                count += leftMax - heights[left]
                
        else:
            right -= 1
            if heights[right] > rightMax:
                rightMax = heights[right]
            else:
                count += rightMax - heights[right]
                
                
# EXPLANATION

def trappingWater(heights):
    # Initialize two pointers: one at the start (left) and one at the end (right) of the heights list.
    left, right = 0, len(heights) - 1
    
    # leftMax and rightMax are the maximum heights encountered so far from the left and right, respectively.
    leftMax, rightMax = heights[left], heights[right]
    
    # Variable 'count' will accumulate the total trapped water.
    count = 0

    # The loop runs while there is at least one space between the left and right pointers.
    while left + 1 < right:
        
        # Compare the maximum heights from both sides.
        # If the right side max is greater than the left side max, we process the left side.
        if rightMax > leftMax:
            left += 1  # Move the left pointer one step to the right.
            
            # Move leftMax if the new height at the left pointer is greater than the current leftMax.
            if heights[left] > leftMax:
                leftMax = heights[left]
            else:
                # If the current height is less than leftMax, it means water can be trapped.
                # The amount of water trapped is the difference between leftMax and the current height.
                count += leftMax - heights[left]
        
        # If rightMax is less than or equal to leftMax, we process the right side.
        else:
            right -= 1  # Move the right pointer one step to the left.
            
            # Move rightMax if the new height at the right pointer is greater than the current rightMax.
            if heights[right] > rightMax:
                rightMax = heights[right]
            else:
                # If the current height is less than rightMax, it means water can be trapped.
                # The amount of water trapped is the difference between rightMax and the current height.
                count += rightMax - heights[right]
    
    # After processing all possible trapped water, return the total amount.
    return count
