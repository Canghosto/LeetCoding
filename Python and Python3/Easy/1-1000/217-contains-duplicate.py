class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] - nums[i + 1] == 0:
                return True
        return False