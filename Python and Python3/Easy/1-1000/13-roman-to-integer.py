class Solution(object):
    def romanToInt(self, s):

        if 1 >= len(s) >= 15:
            return 0
        skip = -1
        res = 0
        for idx, num in enumerate(s):
            if skip == idx:
                continue
            
            if num == "I":
                if len(s) > idx + 1 and s[idx + 1] == "V":
                    res += 4
                    skip = idx + 1
                elif len(s) > idx + 1 and s[idx + 1] == "X":
                    res += 9
                    skip = idx + 1
                else:
                    res += 1
            if num == "V":
                res += 5
            if num == "X":
                if len(s) > idx + 1 and s[idx + 1] == "L":
                    res += 40
                    skip = idx + 1
                elif len(s) > idx + 1 and s[idx + 1] == "C":
                    res += 90
                    skip = idx + 1
                else:
                    res += 10
            if num == "L":
                res += 50
            if num == "C":
                if len(s) > idx + 1 and s[idx + 1] == "D":
                    res += 400
                    skip = idx + 1
                elif len(s) > idx + 1 and s[idx + 1] == "M":
                    res += 900
                    skip = idx + 1
                else:
                    res += 100
            if num == "D":
                res += 500
            if num == "M":
                res += 1000
        return res        