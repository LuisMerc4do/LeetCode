def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashset = set()
    for i in nums:
        if i in hashset: 
            return True
        hashset.add(i)
    return False

print(containsDuplicate([1,2,3,4]))