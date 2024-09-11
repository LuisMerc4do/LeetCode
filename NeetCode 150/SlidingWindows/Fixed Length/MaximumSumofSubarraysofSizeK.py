class Solution:
    def maxSum(self, nums: list[int], k: int):
        state = 0
        start = 0
        max_ = 0

        for end in range(len(nums)):
            state += nums[end]

            if end - start + 1 == k:
                max_ = max(max_, state)
                state -= nums[start]
                start += 1
        return max_