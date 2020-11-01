class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return ["->".join([str(lower), str(upper)])]
        if lower == upper:
            return []
        result =[]
        i = lower
        for n in nums:
            if n == i:
                i += 1
                continue
            else:
                if i == n - 1:
                    result.append(str(i))
                else:
                    result.append("->".join([str(i), str(n - 1)]))
                i = n + 1
        if i == upper:
            result.append(str(i))
        elif i < upper:
            result.append("->".join([str(i), str(upper)]))
        return result
            
