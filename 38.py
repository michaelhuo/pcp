class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSayStr(s: str) -> str:
            if not s:
                return "1"
            output = []
            prev = s[0]
            count = 0
            for c in s:
                if c == prev:
                    count += 1
                else:
                    output.append(chr(ord('0') + count))
                    output.append(prev)
                    prev = c
                    count = 1
            output.append(chr(ord('0') + count))
            output.append(prev)
            return "".join(output)
        
        if n == 0:
            return ""
        else:
            s = ""
            for _ in range(n):
                s = countAndSayStr(s)
            return s
