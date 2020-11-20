class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
            if not primes[i]:
                continue
            for j in range(i * i, n, i):
                primes[j] = False
        count = 0
        for p in primes[2:n]:
            if p:
                count += 1
        return count
                
