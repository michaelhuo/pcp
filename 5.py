class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        odd_set = set(i for i in range(length))
        even_set = set(i for i in range(length - 1) if s[i] == s[i + 1])
        odd_length = 0
        even_length = 0
        tmp_set = set()
        
        for odd_length in range(1, length):
            for i in odd_set:
                if i >= odd_length and i < length - odd_length and s[i - odd_length] == s[i + odd_length]:
                    tmp_set.add(i)
            if tmp_set:
                odd_set = tmp_set
                tmp_set=set()
            else:
                break
            
        odd_length -= 1
        
        for even_length in range(1, length):
            for i in even_set:
                if i >= even_length and i < length - even_length - 1 and s[i - even_length] == s[i + even_length +1]:
                    tmp_set.add(i)
            if tmp_set:
                even_set = tmp_set
                tmp_set = set()
            else:
                break
        even_length -= 1
        print(odd_length, even_length)
        print(odd_set, even_set)
        if odd_set and odd_length > 0 and odd_length * 2 + 1 >= even_length * 2 + 2:
            index = odd_set.pop()
            return s[index - odd_length:index + odd_length + 1]
        elif even_set:
            index = even_set.pop()
            return s[index - even_length:index + even_length + 2]
        else:
            return s[0]
