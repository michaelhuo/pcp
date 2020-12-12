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
            "/": operator.floordiv
        }
        for token in tokens:
            if token in operators:
                oprand2 = oprands.pop()
                oprand1 = oprands.pop()
                op = operators[token]
                if token == '/':
                    is_negative = (oprand1 < 0 and oprand2 > 0) or (oprand1 > 0 and oprand2 < 0)
                    oprand1 = -oprand1 if oprand1 < 0 else oprand1
                    oprand2 = -oprand2 if oprand2 < 0 else oprand2
                    result = op(oprand1, oprand2)
                    if is_negative:
                        result = -result
                else:
                    result = op(oprand1, oprand2)
                oprands.append(result)
            else:
                oprands.append(int(token))
        return oprands.pop()
                
        
