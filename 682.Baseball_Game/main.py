class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for op in ops:
            if op == '+':
                points.append(points[-1] + points[-2])
            elif op == 'D':
                points.append(points[-1] * 2)
            elif op == 'C':
                points.pop()
            else:
                points.append(int(op))

        return sum(points)
