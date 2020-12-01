class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if t != mapping[c]:
                    return False
        if stack:
            return False
        return True
