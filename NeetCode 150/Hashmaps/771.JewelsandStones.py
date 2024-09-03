def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        hashset = set(jewels)
        count = 0
        for j in stones:
            if j in hashset:
                count += 1
        return count 
    
print(numJewelsInStones("aA", "aAAbbbb"))