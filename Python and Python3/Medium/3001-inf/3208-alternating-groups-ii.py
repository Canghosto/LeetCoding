class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count=0
        alternating = 0
        lenCol = len(colors)
        i= 0
        while i < lenCol+ k - 1:
            if colors[i % lenCol] != colors[(i + 1) % lenCol]:
                count += 1
            else:
                count = 1

            if  count >= k:
                alternating += 1
            i += 1
        return alternating