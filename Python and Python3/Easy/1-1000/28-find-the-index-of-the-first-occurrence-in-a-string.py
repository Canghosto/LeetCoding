class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pos = 0
        while pos <= len(haystack) - len(needle):
            if haystack[pos:len(needle) + pos]== needle:
                return pos
            pos += 1
        return -1