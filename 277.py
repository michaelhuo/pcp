# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        excluded = set()
        candidates = set([i for i in range(n)])
        count = 0
        while candidates:
            # print(candidates)
            a = candidates.pop()
            b = candidates.pop()
            # print(a,b)
            add_a = True
            add_b = True
            if knows(a, b):
                excluded.add(a)
                add_a = False
            else:
                excluded.add(b)
                add_b = False
            if knows(b, a):
                excluded.add(b)
                add_b = False
            else:
                excluded.add(a)
                add_a = False
            count += 2
            if add_a:
                # print("add ", a)
                candidates.add(a)
                count -= 1
            if add_b:
                # print("add ", b)
                candidates.add(b)
                count -= 1
            if count == n - 1:
                break
        if count == n - 1:
            is_celebrity = True
            candidate = candidates.pop()
            for i in range(n):
                if not knows(i, candidate):
                    return -1
                if i != candidate and knows(candidate, i):
                    return -1
            return candidate
        else:
            return -1
