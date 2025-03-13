class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counter = 0
        totalCount = 0
        subSum = 0
        i = 0
        hashSub = {}
        ans = []
        for sub in grid:
            while i < len(sub):
                if sub[i] not in hashSub:
                    hashSub[sub[i]] = 1
                    subSum += sub[i]
                else:
                    ans.append(sub[i])

                counter += 1
                totalCount += counter
                i += 1
            i = 0
        ans.append(totalCount - subSum)
        return ans