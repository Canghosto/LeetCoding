class Solution(object):
    def maximumSum(self, nums):

        mx = -1
        hashT = {}
        for x in nums:
            tmp = map(int, str(x))
            sumTmp = sum(tmp)
            if sumTmp not in hashT:
                hashT[sumTmp] = [x]

            elif len(hashT[sumTmp]) == 1:
                hashT[sumTmp].append(x)
                hashT[sumTmp].append(x + hashT[sumTmp][0])
                if mx < hashT[sumTmp][2]:
                    mx = hashT[sumTmp][2]
            else:
                if x > min(hashT[sumTmp]):
                    smaller = hashT[sumTmp].index(min(hashT[sumTmp]))
                    hashT[sumTmp][smaller] = x
                    hashT[sumTmp][2] = hashT[sumTmp][1] + hashT[sumTmp][0]
                    if mx < hashT[sumTmp][2]:
                        mx = hashT[sumTmp][2]

        return mx