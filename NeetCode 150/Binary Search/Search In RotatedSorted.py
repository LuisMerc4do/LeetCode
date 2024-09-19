def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= target:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    


# explanation

def search(nums, target):
    # Initialize two pointers for the binary search
    left = 0
    right = len(nums) - 1

    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # If the middle element is the target, return its index
        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            # If target is within the sorted left half
            if nums[left] <= target < nums[mid]:
                # Move the right pointer to narrow the search to the left half
                right = mid - 1
            else:
                # Otherwise, narrow the search to the right half
                left = mid + 1
        else:
            # If the right half is sorted
            if nums[mid] < target <= nums[right]:
                # If the target is in the sorted right half, move the left pointer
                left = mid + 1
            else:
                # Otherwise, narrow the search to the left half
                right = mid - 1

    # If the target is not found, return -1
    return -1
