class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountA = {}
        charCountB = {}
        if len(s) != len(t):
            return False
        else:
            pos = 0
            while pos < len(s):
                if s[pos] not in charCountA:
                    charCountA[s[pos]] = 1
                else:
                    charCountA[s[pos]] += 1 
                if t[pos] not in charCountB:
                    charCountB[t[pos]] = 1
                else:
                    charCountB[t[pos]] += 1
                pos += 1
        for x in charCountA:
            if x not in charCountB:
                return False
            if charCountA[x] != charCountB[x]:
                return False
        return True
                