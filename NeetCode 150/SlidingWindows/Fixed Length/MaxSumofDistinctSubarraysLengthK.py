class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_sum = 0
        curr_sum = 0
        start = 0
        state = {}

        for end in range(len(nums)):
            curr_sum = curr_sum + nums[end]
            state[nums[end]] = state.get(nums[end], 0) + 1

            if end - start + 1 == k:
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[start]
                state[nums[start]] = state.get(nums[start], 0) - 1
                if state[nums[start]] == 0:
                    del state[nums[start]]
                start += 1
        return max_sum
    
    

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize variables to store the maximum sum found, the current window sum, and the start pointer.
        max_sum = 0         # Stores the maximum sum of a valid subarray of size k.
        curr_sum = 0        # Tracks the sum of the current window (subarray).
        start = 0           # Start pointer of the sliding window.
        state = {}          # Dictionary to store the frequency of each element in the current window.

        # Iterate over the array using 'end' as the end pointer of the window.
        for end in range(len(nums)):
            # Add the current number to the current sum and increment its count in the dictionary.
            curr_sum = curr_sum + nums[end]
            state[nums[end]] = state.get(nums[end], 0) + 1

            # When the window size reaches 'k', process the window.
            if end - start + 1 == k:
                # If all elements in the window are unique (i.e., their counts in the dictionary are all 1),
                # update the maximum sum if the current sum is larger.
                if len(state) == k:
                    max_sum = max(max_sum, curr_sum)

                # Now, slide the window to the right by removing the element at the start of the window.
                curr_sum -= nums[start]
                
                # Decrease the count of the element at 'start' in the dictionary.
                state[nums[start]] = state.get(nums[start], 0) - 1

                # If the count of the element at 'start' is now zero, remove it from the dictionary.
                if state[nums[start]] == 0:
                    del state[nums[start]]
                
                # Move the start pointer to the right.
                start += 1

        # Return the maximum sum found.
        return max_sum
