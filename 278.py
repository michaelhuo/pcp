# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        i, j = 1, n
        while i < j:
            k = i + (j - i) // 2
            if isBadVersion(k):
                j = k
            else:
                i = k + 1
        return j
            
