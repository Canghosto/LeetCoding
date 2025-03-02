class Solution(object):
    def twoSum(self, nums, target):
        secondNums = nums[1:]
        for first in nums:  
            count = nums.index(first) + 1
            for second in secondNums:
                targetSum = first + second
                if targetSum == target:
                    return [nums.index(first), count]
                count += 1
            secondNums = secondNums[1:]