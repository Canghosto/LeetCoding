class Solution(object):
    def scoreOfString(self, s):
        result = 0
        if len(s) == 0:
            return result
        for ind, ch in enumerate(s):
            if ind < len(s) - 1:
                result += abs(ord(s[ind]) - ord(s[ind + 1]))
        return result
        """
        :type s: str
        :rtype: int
        """
        