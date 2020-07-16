class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        row = len(matrix)
        col = len(matrix[0])

        for c in range(col):
            r = 0
            while c + 1 < col and r + 1 < row:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                r += 1
                c += 1

        for r in range(1,row):
            c = 0
            while c + 1 < col and r + 1 < row:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                r += 1
                c += 1

        return True