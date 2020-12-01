class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(parentheses: str, n: int) -> None:
            if not n:
                if parentheses not in answer:
                    answer.append(parentheses)
            else:
                size = len(parentheses)
                if not size:
                    s = "()"
                    backtracking(s, n - 1)
                else:
                    ss = set()
                    for i in range(size):
                        s = parentheses[:i + 1] + "()" + parentheses[i + 1:]
                        if s not in ss:
                            ss.add(s)
                            backtracking(s, n - 1)
        backtracking("", n)
        return answer
