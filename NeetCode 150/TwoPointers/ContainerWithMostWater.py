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