class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if not A or not B or not C or not D:
            return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        AB = [i+j for i in A for j in B]
        CD = [i+j for i in C for j in D]
        AB.sort()
        CD.sort()
        hash_map = {}
        for i,n in enumerate(CD):
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        length = len(A)
        count = 0
        for i,ab in enumerate(AB):
            cd = -ab
            if cd in hash_map:
                count += hash_map[cd]
        return count

