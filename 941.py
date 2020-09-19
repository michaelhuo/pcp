class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length = len(A)
        if length < 3:
            return False
        for i in range(1, length):
            if A[i] <= A[i - 1]:
                break
        max = i - 1
        for i in range(length - 2, -1, -1):
            if A[i] <= A[i + 1]:
                break
        return max == i + 1