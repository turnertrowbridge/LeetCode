class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        symbols = {
            "+": lambda n1, n2: n2 + n1,
            "-": lambda n1, n2: n2 - n1,
            "*": lambda n1, n2: n2 * n1,
            "/": lambda n1, n2: int(n2 / n1)
        }



        for c in tokens:
            if c in symbols:
                n1 = stack.pop()
                n2 = stack.pop()
                s = symbols[c]
                stack.append(s(n1, n2))
            else:
                stack.append(int(c))

        return stack.pop()
                    


        

            
