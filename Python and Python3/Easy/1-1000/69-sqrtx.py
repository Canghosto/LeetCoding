class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, int(x/2 + 1)):
            if  i * i <= x and (i + 1) * (i + 1) > x:
                return int(i)
        return 0 if x == 0 else 1
        