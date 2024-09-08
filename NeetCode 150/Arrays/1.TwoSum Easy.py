nums = [2,7,11,15]
target = 9
left = 0
right = len(nums) - 1
while left < right:
     sum = nums[left] + nums[right]
     if sum == target:
          print("true")
     if sum < target:
          left += 1
     else:
          right -= 1