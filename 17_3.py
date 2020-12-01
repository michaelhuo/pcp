class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        answer = []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def backtracking(predigits: str, nextdigits: str) -> None:
            if not nextdigits:
                answer.append(predigits)
            else:
                for c in mapping[nextdigits[0]]:
                    backtracking(predigits + c, nextdigits[1:])
        backtracking("", digits)
        return answer
                
