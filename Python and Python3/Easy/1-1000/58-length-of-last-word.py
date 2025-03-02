class Solution(object):
    def lengthOfLastWord(self, s):
        array = s.split(" ")
        for i in reversed(array):
            if len(i) != 0:
                return len(i)