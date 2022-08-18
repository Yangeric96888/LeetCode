class Solution:
    def isValid(self, s: str) -> bool:

        legend = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in legend:
                if stack and stack[-1] == legend[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if len(stack) == 0 else False
