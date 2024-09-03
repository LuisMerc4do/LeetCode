def topKFrequent(nums, k):
    counter = {}
    for i in nums: 
        if i in counter: 
            counter[i] += 1
        else:
            counter[i] = 1
            
print(topKFrequent(nums = [1,1,1,2,2,3], k=2))
 