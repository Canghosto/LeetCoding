class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        lastZero = len(nums) - 1
        while i < lastZero:
            if nums[lastZero] == 0:
                lastZero -= 1
            else:
                if nums[i] == 0:
                    del nums[i]    
                    lastZero -= 1
                    nums.append(0)   
                    continue
                elif nums[i] == nums[i+1] and nums[i] != 0:
                    nums[i] = nums[i] * 2
                    del nums[i+1]
                    lastZero -= 1
                    nums.append(0)
                i += 1
        return nums