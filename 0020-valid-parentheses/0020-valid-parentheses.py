class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
                    ")": "(", 
                    "}": "{",
                     "]": "["
                    }

        char_stack = []

        for c in s:
            # add to stack if it's not a closing bracket
            if c not in char_map:
                char_stack.append(c)

            # stack is empty or top of stack is not a closing bracket
            elif not char_stack or char_stack[-1] != char_map[c]:
                return False
                
            else:
                char_stack.pop()

        return not char_stack



