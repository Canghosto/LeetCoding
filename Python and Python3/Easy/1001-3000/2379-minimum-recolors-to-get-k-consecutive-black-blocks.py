class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minb = 0
        for b in range(len(blocks) - k + 1):
            curr_sub = blocks[b: b+ k]
            minSub = curr_sub.count('W')
            if minSub == 0:
                return minSub
            if minb == 0:
                minb = minSub
            elif minb > minSub:
                minb = minSub
                
        return minb