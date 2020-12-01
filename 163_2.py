class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def range_tostr(low: int, high: int) -> str:
            if low == high:
                return str(low)
            else:
                return "{}->{}".format(low, high)
        if not nums:
            return [range_tostr(lower, upper)]
        answer = []
        for n in nums:
            if n > lower:
                answer.append(range_tostr(lower, n - 1))
            lower = n + 1
        if lower <= upper:
            answer.append(range_tostr(lower, upper))
        return answer
        
