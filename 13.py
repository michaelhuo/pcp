class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        prev = ""
        values = {"I": 1, "V" : 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        size = len(s)
        if size == 1:
            return values[s]
        i = 0
        while i < size - 1:
            if values[s[i]] < values[s[i + 1]]:
                ans += values[s[i + 1]] - values[s[i]]
                i += 2
            else:
                ans += values[s[i]]
                i += 1
        if i == size - 1:
            ans += values[s[i]]
        return ans
                    
                
            
