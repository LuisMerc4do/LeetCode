class Solution:
    def triangleNumber(self, heights: list[int]):
        heights.sort()
        count = 0
        for i in range(len(heights) - 1, 1, -1):
            left = 0 
            right = i - 1
            while left < right:
                if heights[left] + heights[right] > heights[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count




#  EXPLANATION

class Solution:
    def triangleNumber(self, heights: list[int]):
        # Step 1: Sort the input list. This helps us efficiently find valid triangles
        # by leveraging the triangle inequality property.
        heights.sort()
        
        # Variable 'count' to keep track of the number of valid triangles.
        count = 0
        
        # Step 2: Traverse the sorted list starting from the last element (heights[i]).
        # The idea is to fix the largest number as 'heights[i]' and find two other numbers
        # such that heights[left] + heights[right] > heights[i].
        for i in range(len(heights) - 1, 1, -1):
            # Initialize two pointers: 'left' at the start and 'right' just before 'i'.
            left = 0
            right = i - 1

            # Step 3: Use a two-pointer technique to find valid triangles.
            while left < right:
                # If the sum of heights[left] and heights[right] is greater than heights[i],
                # then all pairs between left and right can form a valid triangle with heights[i].
                if heights[left] + heights[right] > heights[i]:
                    # Add (right - left) because all elements from 'left' to 'right-1' can
                    # pair with heights[right] to form valid triangles.
                    count += right - left
                    # Move the 'right' pointer leftward to check the next smaller pair.
                    right -= 1
                else:
                    # If heights[left] + heights[right] <= heights[i], move the 'left' pointer rightward
                    # because we need larger values to meet the triangle inequality.
                    left += 1

        # Step 4: Return the total count of valid triangles.
        return count
