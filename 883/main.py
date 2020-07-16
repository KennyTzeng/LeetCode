class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # xy
        area1 = 0
        for row in grid:
            for number in row:
                if number > 0:
                    area1 += 1

        # xz - sum of every maxinum of every row
        area2 = sum(list(map(max, grid)))

        # yz - sum of every maxinum of every column
        area3 = sum(list(map(max, zip(*grid))))

        return area1 + area2 + area3
