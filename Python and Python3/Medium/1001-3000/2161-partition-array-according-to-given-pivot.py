class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        beginning = []
        end = []
        mid = []
        for i in nums:
            if i > pivot:
                end.append(i)
            elif i < pivot:
                beginning.append(i)
            else:
                mid.append(i)

        return beginning + mid + end