class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n: int) -> int:
            if n <= 0:
                m[0] = 0 
                return 0
            elif n == 1:
                m[1] = 1
                return 1
            elif n == 2:
                m[2] = 1
                return 1
            else:
                n3, n2, n1 = n - 3, n - 2, n - 1
                t3, t2, t1 = 0, 0, 0
                if n3 in m:
                    t3 = m[n3]
                else:
                    t3 = helper(n3)
                    m[n3] = t3
                if n2 in m:
                    t2 = m[n2]
                else:
                    t2 = helper(n2)
                    m[n2] = t2
                if n1 in m:
                    t1 = m[n1]
                else:
                    t1 = helper(n1)
                    m[n1] = t1
                return t3 + t2 + t3
            
            m = [-1] * n
            return helper(n)
