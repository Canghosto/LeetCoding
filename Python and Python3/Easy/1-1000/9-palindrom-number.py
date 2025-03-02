class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        xAsString = str(x)
        
        for i in range(0, (len(str(x))/2)):
            if (xAsString[i] != xAsString[len(xAsString)-1-i]):
                return False
        return True