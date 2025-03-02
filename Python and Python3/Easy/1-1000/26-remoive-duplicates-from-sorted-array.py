class Solution(object):
    def removeDuplicates(self, nums):

        count = 0
        
        for idx, x in enumerate(nums):
            if len(nums) == idx + 1:
                nums[count] = x
                count = count + 1
            elif nums[idx] < nums[idx + 1]:
                nums[count] = x
                count = count + 1
        return count