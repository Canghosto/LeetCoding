class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        firstNr = int(nums[0], 2)
        size = len(nums[0])
        binaryMax = (2 ** size) - 1

        mapped = list(map(lambda x: int(x, 2), nums))
        pos = firstNr + 1
        if pos > binaryMax:
            pos = 0
        
        while firstNr is not pos:
            if pos not in mapped:
                return bin(pos)[2:].zfill(size)
            pos += 1
            if pos >= binaryMax:
                pos = 0