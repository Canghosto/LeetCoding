class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashPairs = {}
        count = 0
        for num in nums:
            if num not in hashPairs:
                hashPairs[num] = 1
                count += 1
            else:
                hashPairs[num] += 1
                if hashPairs[num] % 2:
                    count += 1
                else:
                    count -= 1
                    
        return True if count == 0 else False