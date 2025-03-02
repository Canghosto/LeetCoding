class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits[-1] += 1
        i = -1
        while digits[i] > 9:
            rest = digits[i] - 10
            digits[i] = rest
            i -= 1
            if len(digits) < -i:
                digits.insert(0, 1)
            else:
                digits[i] += 1

        return digits