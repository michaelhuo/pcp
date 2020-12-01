class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def backtracking(digits: str, key: str) -> List[str]:
            answer = []
            if not digits:
                if not key:
                    return answer
            for c in mapping[key]:
                answer.append(digits + c)
            return answer
        answer = ["",]
        predigits = ""
        for key in digits:
            level = []
            for predigits in answer:
                level += backtracking(predigits, key)
            answer = level
        return answer
                
