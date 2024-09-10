#2 POINTERS

class Solution:
    def sortColors( nums: list[int]):
        left, right = 0, len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        return nums 
    
    
    # BUBBLE SORT
class Solution:
    def sortColors(self, nums: list[int]):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums
            
    nums = [2,0,2,1,1,0]
    print(sortColors(nums))



#### COMMENTED

class Solution:
    def sortColors(nums: list[int]):
        # Initialize two pointers: 'left' at the beginning and 'right' at the end of the list.
        left, right = 0, len(nums) - 1
        i = 0  # Pointer 'i' will be used to traverse the array.

        # Traverse the list with the 'i' pointer until it crosses the 'right' pointer.
        while i <= right:
            # Case 1: If the current element is 0, we need to move it to the left.
            if nums[i] == 0:
                # Swap the current element with the element at the 'left' pointer.
                nums[i], nums[left] = nums[left], nums[i]
                # Move the 'left' pointer to the right and the 'i' pointer to the right.
                left += 1
                i += 1
            # Case 2: If the current element is 2, we need to move it to the right.
            elif nums[i] == 2:
                # Swap the current element with the element at the 'right' pointer.
                nums[i], nums[right] = nums[right], nums[i]
                # Move the 'right' pointer to the left, but we don't increment 'i' here.
                # This is because the swapped element needs to be processed.
                right -= 1
            # Case 3: If the current element is 1, it is already in the correct place.
            # Just move the 'i' pointer to the right.
            else:
                i += 1

        # Return the sorted list (in-place sorting, but returning it for clarity).
        return nums

# Test the solution with an example.
nums = [2, 0, 2, 1, 1, 0]
print(Solution.sortColors(nums))  # Output will be a sorted list: [0, 0, 1, 1, 2, 2]



## BUBBLE SORT

class Solution:
    def sortColors(self, nums: list[int]):
        # Outer loop to control the number of passes (n-1 passes in total).
        for i in range(len(nums) - 1):
            # Inner loop for comparing adjacent elements and pushing larger values to the end.
            for j in range(len(nums) - i - 1):
                # If the current element is greater than the next one, swap them.
                if nums[j] > nums[j + 1]:
                    temp = nums[j]  # Store the current element in a temporary variable.
                    nums[j] = nums[j + 1]  # Move the smaller element to the left.
                    nums[j + 1] = temp  # Place the larger element to the right.

        # Return the sorted list (in-place sorting).
        return nums

# Test the solution with an example.
nums = [2, 0, 2, 1, 1, 0]
print(Solution().sortColors(nums))  # Output will be a sorted list: [0, 0, 1, 1, 2, 2]
