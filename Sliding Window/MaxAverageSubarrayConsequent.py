def AverageOfSubarrayOfSizeK(k, arr):
    result = []  # Initialize as an empty list
    windowSum = 0  # Variable to keep track of the sum of the current window
    windowStart = 0  # The start index of the sliding window

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # Add the next element to the window sum
        
        if windowEnd >= k - 1:  # Check if the window has reached size k
            result.append(windowSum / k)  # Calculate the average and store it in the result list
            windowSum -= arr[windowStart]  # Subtract the element going out of the window
            windowStart += 1  # Move the window ahead
    
    return result  # Return the list of averages

# Example usage:
print(AverageOfSubarrayOfSizeK(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
