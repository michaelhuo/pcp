class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(s: str, n_left: int, n_right: int) -> None:
            if not n_left and not n_right:
                answer.append(s)
            else:
                if n_left > 0:
                    backtracking(s + "(", n_left - 1, n_right)
                if n_right > n_left:
                    backtracking(s + ")", n_left, n_right - 1)
        if n == 0:
            return []
        elif n == 1:
            return ["()",]
        backtracking("", n, n)
        return answer
