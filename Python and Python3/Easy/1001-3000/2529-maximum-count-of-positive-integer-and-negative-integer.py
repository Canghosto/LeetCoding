class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negative = 0
        positiv = 0
        for i in nums:
            if i == 0:
                continue
            if i < 0:
                negative += 1
            elif i> 0:
                positiv += 1
        return max(positiv, negative)