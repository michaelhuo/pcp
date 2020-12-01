class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def helper(digits: str) -> List[str]:
            if not digits:
                return []
            print(digits)
            if len(digits) == 1:
                return [c for c in mapping[digits]]
            l1 = helper(digits[0])
            l2 = helper(digits[1:])
            d = digits[0]
            answer = []
            for d1 in l1:
                for d2 in l2:
                    answer.append(d1 + d2)
            return answer
        return helper(digits)
                `
