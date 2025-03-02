class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNr = {}
        for n in nums:
            if n not in hashNr:
                hashNr[n] = 1
            else:
                hashNr[n] += 1
        pos = 0
        sorteditemsHighest = sorted(hashNr.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range (k):
            print(i)
            res.append(sorteditemsHighest[i][0])
        return res
