class Solution(object):
    def addBinary(self, a, b):

        totalInt = int(a, 2) + int(b, 2)
        return bin(totalInt)[2:]