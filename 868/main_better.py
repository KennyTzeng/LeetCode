class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        indexes_1 = [ i for i, digit in enumerate(bin(N)[2:]) if digit == '1' ]
        
        if len(indexes_1) <= 1:
            return 0
        else:
            return max([indexes_1[i] - indexes_1[i-1] for i in range(1, len(indexes_1))])