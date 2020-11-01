class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        sign = 1
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        is_digit = False
        has_sign = False

        for c in s:
            if not is_digit and c == ' ':
                continue
            if c == '+' or c == '-':
                if not is_digit and not has_sign:
                    has_sign = True
                    is_digit = True
                    if c == '-':
                        sign = -1
                else:
                    break
            elif '0' <= c <= '9':
                if not is_digit:
                    is_digit = True
                    result = ord(c) - ord('0')
                else:
                    if result  > INT_MAX // 10:
                        if sign == 1:
                            return INT_MAX
                        else:
                            return INT_MIN
                    else:
                        result = result * 10 + ord(c) - ord('0')
            else:
                break
        result = sign * result
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
                        
