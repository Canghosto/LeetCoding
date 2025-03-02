class Solution(object):
    def removeOccurrences(self, s, part):
        i = 0

        while part in s:
            s = s.replace(part, '', 1)

        return s