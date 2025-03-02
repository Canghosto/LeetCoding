class Solution(object):
    def threeSum(self, nums):

        threeSumList = []
        nums.sort()
        size = len(nums)

        for firstPos in range(len(nums) - 2):    
            if firstPos > 0 and nums[firstPos - 1] == nums[firstPos]:
                continue   

            secondPos = firstPos + 1
            thirdPos = size - 1

            while secondPos < thirdPos:

                if secondPos > firstPos + 1 and nums[secondPos - 1] == nums[secondPos]:
                    secondPos = secondPos + 1
                    continue   
                
                if thirdPos < size - 1 and nums[thirdPos + 1] == nums[thirdPos]:
                    thirdPos = thirdPos - 1
                    continue   
                
                totalSum3 = nums[firstPos] + nums[secondPos] + nums[thirdPos]

                if totalSum3 == 0:
                    threeSumList.append([nums[firstPos], nums[secondPos], nums[thirdPos]])
                    secondPos = secondPos + 1
                    thirdPos = thirdPos - 1
                elif totalSum3 < 0:
                    secondPos = secondPos + 1
                elif totalSum3 > 0:
                    thirdPos = thirdPos - 1

        return threeSumList