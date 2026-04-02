class Solution:
    def isValid(self, s: str) -> bool:
        
        # # Create a truth table
        # mapping = {
        #     "(": ")",
        #     "{": "}", 
        #     "[": "]"
        # }

        # if len(s)%2 == 1:
        #     return False
        # else:
        #     for i in range(int(len(s)/2)):
        #         char = s[i]
        #         if char not in mapping:
        #             return False
        #         elif mapping[char] != s[-(i+1)]:
        #             return False
        
        # return True

        stack = []
        mapping = {
            ")": "(",
            "}": "{", 
            "]": "["
        }

        for c in s:
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return not stack

