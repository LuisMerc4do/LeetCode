class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hasSeen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hasSeen: 
                return [hasSeen[diff], i]
            hasSeen[nums[i]] = i