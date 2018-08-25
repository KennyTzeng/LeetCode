class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose_matrix = []
        for row in zip(*A):
            transpose_matrix.append(list(row))
        return transpose_matrix