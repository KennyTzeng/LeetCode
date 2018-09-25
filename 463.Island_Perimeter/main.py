class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        perimeter = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    count = 0
                    if x - 1 >= 0 and grid[y][x-1]:
                        count += 1
                    if y - 1 >= 0 and grid[y-1][x]:
                        count += 1
                    if x + 1 < len(grid[0]) and grid[y][x+1]:
                        count += 1
                    if y + 1 < len(grid) and grid[y+1][x]:
                        count += 1
                    perimeter += (4 - count)
        
        return perimeter
