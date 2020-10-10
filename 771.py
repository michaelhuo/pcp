class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0

        jewels = dict((k,0) for k in J)
        
        for stone in S:
            if stone in jewels:
                jewels[stone] += 1
        
        count = 0        
        for n in jewels.values():
            count += n
        return count
        
