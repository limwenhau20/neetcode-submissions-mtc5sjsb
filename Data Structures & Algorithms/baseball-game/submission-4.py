class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for s in operations:
            if s == "+":
                arr.append(int(arr[-1]) + int(arr[-2]))
            elif s == "C":
                arr.pop()
            elif s == "D":
                arr.append(int(arr[-1]) * 2)
            else:
                arr.append(int(s))
        return sum(arr)
