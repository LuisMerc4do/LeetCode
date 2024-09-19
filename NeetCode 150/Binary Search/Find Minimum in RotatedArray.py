def findMin (nums):
    result = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] < nums[right]:
            result = min(res, nums[l])
            break
        
        mid = (left + right) // 2
        result = min(res, nums[mid])
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return result     

# EXPLAINED

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1
        # Initialize result with the first element of the array
        result = nums[0]

        # Continue searching as long as left pointer is less than or equal to right pointer
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            # Update result to keep track of the minimum found so far
            result = min(result, nums[mid])

            # If the middle element is greater than the rightmost element
            if nums[mid] > nums[right]:
                # The minimum is in the right half, so move the left pointer
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half, so move the right pointer
                right = mid - 1

        # Return the smallest element found
        return result
