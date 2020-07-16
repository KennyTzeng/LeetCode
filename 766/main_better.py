class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) == 1:
            return True
        
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row-1][col-1] != matrix[row][col]:
                    return False
        
        return True