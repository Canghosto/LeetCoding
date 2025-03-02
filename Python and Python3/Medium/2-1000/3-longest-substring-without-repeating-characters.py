class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longestString = ''
        tmp = ''
        i = 0
        j = i
        while i < len(s) and j < len(s):
            if s[j] in tmp :
                i = i + 1
                j = i
                if len(tmp) > len(longestString):
                    longestString = tmp
                tmp = ''
            else:
                tmp +=s[j]
                j = j + 1
        return len(longestString) if len(tmp) < len(longestString) else len(tmp)