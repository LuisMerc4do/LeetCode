nums = [2,7,11,15]
target = 9
hasSeen = {}
for item in range(len(nums)):
    diff = target - nums[item]
    if diff in hasSeen:
         print([diff, nums[item]])
    hasSeen[nums[item]] = item

           dw
