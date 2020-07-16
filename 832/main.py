class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        flipped_A = []
        for row in A:
            flipped_row = []
            row.reverse()
            for bit in row:
                if bit:
                    flipped_row.append(0)
                else:
                    flipped_row.append(1)
            flipped_A.append(flipped_row)

        return flipped_A
