class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        count = 0
        row_max = list(map(max, grid))
        col_max = list(map(max, zip(*grid)))

        return sum(min(i,j) for i in row_max for j in col_max) - sum(map(sum, grid))