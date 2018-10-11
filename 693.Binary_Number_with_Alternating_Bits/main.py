class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        bin_n = bin(n)[2:]
        for i in range(0,len(bin_n)-1):
            if bin_n[i] == bin_n[i+1]:
                return False
        
        return True
