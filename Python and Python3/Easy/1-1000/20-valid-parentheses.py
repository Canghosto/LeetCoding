class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif ord(stack[-1]) + 1 == ord(char) or ord(stack[-1]) + 2 == ord(char):
                stack.pop()
            else:
                stack.append(char)

        if len(stack) > 0:
            return False
        return True