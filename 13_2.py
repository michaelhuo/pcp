class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V" : 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        size = len(s)
        total = values[s[-1]]
        if size == 1:
            return values[s]
        i = 0
        for i in reversed(range(size - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total
                    
                
            
