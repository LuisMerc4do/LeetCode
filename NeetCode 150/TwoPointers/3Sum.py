class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
    
    
#### EXPLANATION

class Solution:
    def threeSum(self, nums):
        # Step 1: Sort the input list to make it easier to avoid duplicates
        # and use the two-pointer technique.
        nums.sort()
        
        # Initialize an empty list to store the results (triplets).
        result = []
        
        # Step 2: Iterate through the sorted list. We stop at len(nums) - 2
        # because we need at least three numbers for a valid triplet.
        for i in range(len(nums) - 2):
            # Skip duplicate values for the current number 'nums[i]' to avoid
            # adding the same triplet multiple times.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 3: Use the two-pointer technique to find the other two numbers.
            # 'left' pointer starts just after 'i', and 'right' starts at the end of the list.
            left = i + 1
            right = len(nums) - 1
            
            # Continue while the two pointers do not overlap.
            while left < right:
                # Calculate the sum of the three numbers: nums[i], nums[left], and nums[right].
                total = nums[i] + nums[left] + nums[right]
                
                # Case 1: If the sum is less than zero, we need a larger sum, so we move the 'left' pointer to the right.
                if total < 0:
                    left += 1
                
                # Case 2: If the sum is greater than zero, we need a smaller sum, so we move the 'right' pointer to the left.
                elif total > 0:
                    right -= 1
                
                # Case 3: If the sum equals zero, we've found a valid triplet.
                else:
                    # Add the triplet to the result list.
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward, but first skip over any duplicate values
                    # to avoid adding the same triplet multiple times.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers after finding a valid triplet.
                    left += 1
                    right -= 1
        
        # Step 4: Return the list of triplets that sum to zero.
        return result
