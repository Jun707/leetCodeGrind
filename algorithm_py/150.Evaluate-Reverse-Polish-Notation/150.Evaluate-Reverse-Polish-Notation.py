class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token == "+":
                temp1 = res.pop()
                temp2 = res.pop()
                res.append(temp1 + temp2)
            elif token == "*":
                temp1 = res.pop()
                temp2 = res.pop()
                res.append(temp1 * temp2)
            elif token == "-":
                temp1 = res.pop()
                temp2 = res.pop()
                res.append(temp2 - temp1)
            elif token == "/":
                temp1 = res.pop()
                temp2 = res.pop()
                res.append(int(temp2/temp1))
            else:
                res.append(int(token))
        return res[0]
        