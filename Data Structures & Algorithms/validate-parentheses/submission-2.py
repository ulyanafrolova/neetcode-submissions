class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        stack = []
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False
        if not stack:
            return True
        return False