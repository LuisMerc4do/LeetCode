def binary_search(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1

def binary_search(nums, target):
    # Start by setting 'left' to the first index and 'right' to the last index of the list
    left = 0
    right = len(nums) - 1

    # Keep searching while the left index is less than or equal to the right index
    while left <= right:
        # Find the middle index of the current range
        mid = (left + right) // 2
        
        # If the middle element is the target, return the index
        if nums[mid] == target:
            return mid
        
        # If the middle element is less than the target, search the right half
        if nums[mid] < target:
            left = mid + 1  # Move the left boundary to the right, ignoring the left half
        else:
            # If the middle element is greater than the target, search the left half
            right = mid - 1  # Move the right boundary to the left, ignoring the right half
    
    # If the target is not found in the list, return -1
    return -1
