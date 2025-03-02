class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums[0] >= target:
            return 0
        elif nums[len(nums) - 1] == target:
            return len(nums) - 1
        elif nums[len(nums) - 1] < target:
            return len(nums)
        else:
            if nums[int(len(nums)/2)] < target:
                return int(len(nums)/2) + self.searchInsert(nums[int(len(nums)/2):], target)
            elif nums[int(len(nums)/2)] == target:
                return int(len(nums)/2)
            else:
                return self.searchInsert(nums[:int(len(nums)/2) ], target)