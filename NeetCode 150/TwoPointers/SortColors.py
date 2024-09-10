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

