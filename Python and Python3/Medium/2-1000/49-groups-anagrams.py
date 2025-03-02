class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashAscii = {}
        res = []
        for idx, s in enumerate(strs):
            
            sortedStr = ''.join(sorted(s))
            if sortedStr not in hashAscii:
                hashAscii[sortedStr] = [strs[idx]]
            else:
                hashAscii[sortedStr] += [strs[idx]]

        for x in hashAscii.items():
            res.append(x[1])
            

        return res