class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char not in (')', '}', ']'):
                arr.append(char)
            elif arr and char == ')' and arr[-1] == '(':
                arr.pop()
            elif arr and char == '}' and arr[-1] == '{':
                arr.pop()
            elif arr and char == ']' and arr[-1] == '[':
                arr.pop()
            else:
                return False

        return False if arr else True