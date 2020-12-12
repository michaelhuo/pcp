class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return "0"
        negative = False
        if numerator < 0:
            numerator = -numerator
            negative = True
        if denominator < 0:
            denominator = -denominator
            negative = not negative
        quotient, remainder = divmod(numerator, denominator)
        digits = []
        nums = {}
        loop = -1
        index = 0
        while remainder:
            if remainder in nums:
                loop = nums[remainder]
                break
            nums[remainder] = index
            index += 1
            digit, remainder = divmod(remainder * 10, denominator)
            digits.append(str(digit))
        if negative:
            ans = "-" + str(quotient)
        else:
            ans = str(quotient)
        if not digits:
            return ans
     
        if loop == -1:
            return ans + "." + "".join(digits)
        else:
            return ans + "." + "".join(digits[:loop]) + "(" + "".join(digits[loop:]) + ")"
        
