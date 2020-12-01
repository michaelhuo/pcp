class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        size = len(A)
        if size < 2:
            return -1
        A.sort()
        value = 0
        low, high = 0, size - 1
        S = -1
        while low < high:
            value = A[low] + A[high]
            if value == K - 1:
                return K - 1
            elif value >= K:
                high -= 1
            else:
                if value > S:
                    S = value
                low += 1
        return S
