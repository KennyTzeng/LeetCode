class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_N = bin(N)[2:]
        count, maximum = 0, 0
        for index in range(bin_N.index('1')+1, len(bin_N)):
            count += 1
            if bin_N[index] == '1':
                if count > maximum:
                    maximum = count
                count = 0

        return maximum