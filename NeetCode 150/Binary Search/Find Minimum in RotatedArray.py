def findMin (nums):
    result = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        if nums[left] < nums[right]:
            result = min(res, nums[l])
            break
        
        mid = (left + right) // 2
        result = min(res, nums[left])
        
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return result     