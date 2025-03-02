class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        #This was neetcodes solution

        count = 0
        even = 0
        odd = 0
        cur = 0

        modulo = 10**9 + 7

        for i in arr:
            cur += i
            
            if cur % 2:
                count = (count + 1 + even) % modulo
                odd += 1
            else:
                count = (count + odd) % modulo
                even += 1

#        while i < len(arr):
#            
#            nextItem = i + 1
#            
#            nthCount = arr[i]
#
#            if nthCount % 2:
#                count += 1
#
#
#            while nextItem < len(arr):
#                nthCount += arr[nextItem]
#                if nthCount % 2:
#                    count += 1
#                nextItem += 1
#
#            i += 1
#
#        count = count % modulo

        return count