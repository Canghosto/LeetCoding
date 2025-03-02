class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        newArray = []
        newArrayRev = []
        size = len(nums)

        totalProd = 1
        for num in range(-1, size-1):

            if num == -1:
                newArray.append(1)
            else:
                totalProd *= nums[num]
                newArray.append(totalProd)

        totalProd = 1
        revNums = list(reversed(nums))

        for numrev in range(-1, size - 1):

            if numrev == -1:
                newArrayRev.append(1)
            else:
                totalProd *= revNums[numrev]
                newArrayRev.append(totalProd)
        
        answer = [newArrayRev[-i -1] * newArray[i] for i in range(size)]

        return answer
