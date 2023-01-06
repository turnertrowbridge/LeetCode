class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def recursiveDFS(open_n, closed_n):
            if open_n == closed_n == n:
                result.append("".join(stack))
                return
            
            if open_n < n:
                stack.append("(")
                recursiveDFS(open_n + 1, closed_n)
                stack.pop()
            
            if open_n > closed_n:
                stack.append(")")
                recursiveDFS(open_n, closed_n + 1)
                stack.pop()
        
        recursiveDFS(0, 0)
        return result
