class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for i in primes:
                if i * i > n:
                    break
                
                if n % i == 0:
                    return False
            return True
        
        if n <= 2:
            return 0
        primes = [2]
        for i in range(3, n):
            if is_prime(i):
                primes.append(i)
        return len(primes)
