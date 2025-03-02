class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ax = abs(x)
        strx = str(ax)
        rsx = strx [::-1]
        if x > 0:
            retX = int(rsx)
        elif x <= 0:
            retX = -int(rsx)
        if not (-pow(2,31) <= retX <= (pow(2,31) - 1)):
            return 0
            
        return retX

