class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        res = ''
        for idx, x in enumerate(shortest):
            shared = [item[idx] for item in strs]
            if (len(set(shared))== 1):
                res += shared[0]
            else:
                break
        return res