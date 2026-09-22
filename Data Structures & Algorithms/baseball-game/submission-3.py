class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i, n in enumerate(operations):
            if n == "+":
                ans = res[-2] + res[-1]
                res.append(int(ans))
            elif n == "D":
                ans = 2 * res[-1]
                res.append(int(ans))
            elif n == "C":
                res.pop()
            else:
                res.append(int(n))

        return sum(res)
