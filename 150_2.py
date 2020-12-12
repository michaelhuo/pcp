import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        oprands = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for token in tokens:
            if token in operators:
                oprand2 = oprands.pop()
                oprand1 = oprands.pop()
                op = operators[token]

                result = op(oprand1, oprand2)
                if token == '/':
                    result = int(result)
                oprands.append(result)
            else:
                oprands.append(int(token))
        return oprands.pop()
                
        
