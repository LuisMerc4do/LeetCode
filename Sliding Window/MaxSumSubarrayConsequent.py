def AverageOfSubarrayOfSizeK(k, arr):
    result = []
    windowSum = 0
    windowStart = 0 
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            result.append(windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result

print(AverageOfSubarrayOfSizeK(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
