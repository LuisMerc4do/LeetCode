class Solution(object):
    def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hasSeen = set()

        for item in nums:
            if item in hasSeen:
                return True
            hasSeen.add(item)
        return False
    array = [1, 2, 3, 1]
    print(containsDuplicate(nums=array))
    
