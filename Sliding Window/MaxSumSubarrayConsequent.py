def AverageOfSubarrayOfSizeK(k, arr):
    maxSum = 0
    windowSum = 0
    windowStart = 0 
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart] 
            
            windowStart += 1
    return maxSum

print(AverageOfSubarrayOfSizeK(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
