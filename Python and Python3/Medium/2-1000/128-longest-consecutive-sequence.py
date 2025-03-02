class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxCount = 1
        count= 1
        for idx in range(len(nums) - 1):
            if nums[idx + 1] == nums[idx] + 1:
                count += 1
            elif nums[idx + 1] == nums[idx]:
                continue
            else:
                count = 1
            if count > maxCount:
                maxCount = count
        return maxCount if len(nums) > 0 else 0