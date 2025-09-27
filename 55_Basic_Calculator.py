class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [1]   # pila de signos (contexto global inicia como +)
        sign = 1      # signo actual
        result = 0
        i = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
                continue  # evitar i += 1 extra
            elif char == '+':
                sign = stack[-1] * 1
            elif char == '-':
                sign = stack[-1] * -1
            elif char == '(':
                stack.append(sign)
            elif char == ')':
                stack.pop()

            i += 1

        return result
        