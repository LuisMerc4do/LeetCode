def largest_rectangle_area(heights):
  stack = []  # This stack will store the indices of the bars' heights
  max_area = 0  # We start with a maximum area of 0
  i = 0  # This is the index for looping through the heights
  while i < len(heights):
    if not stack or heights[i] >= heights[stack[-1]]:
      stack.append(i)
      i += 1
    else:
      top = stack.pop()  # Get the index of the last height from the stack
      right = i - 1  # Set the current bar as the right boundary
      left = stack[-1] if stack else -1  # Set the left boundary; if the stack is empty, it's -1
      area = heights[top] * (right - left)  # Calculate the area of the rectangle
      max_area = max(max_area, area)  # Update max_area if the new area is larger
  while stack:
    top = stack.pop()
    width = i - stack[-1] - 1 if stack else i
    area = heights[top] * width
    max_area = max(max_area, area)
  return max_area