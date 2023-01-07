class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:        
                if o == "+" and len(stack) > 1:
                    s1 = stack.pop()
                    s2 = stack.pop()
                    stack.append(s2)
                    stack.append(s1)
                    stack.append(s1 + s2)

                elif o == "D" and stack:
                    s1 = stack.pop()
                    stack.append(s1)
                    stack.append(s1 * 2)

                elif o == "C" and stack:
                    stack.pop()
                else: 
                    stack.append(int(o))
                

        return sum(stack)