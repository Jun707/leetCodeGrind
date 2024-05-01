class Solution:
    def isValid(self, s: str) -> bool:
        sDicts = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for i in s:
            if i in sDicts:
                if stack and stack[-1] == sDicts[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        return False