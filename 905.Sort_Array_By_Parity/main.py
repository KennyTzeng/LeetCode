class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        i, j = 0, len(A)-1
        while i < j:
            # to find the next odd number
            while not A[i] % 2 and i < len(A)-1:
                i += 1
            # to find the next even number
            while A[j] % 2 and j > 0:
                j -= 1
            # swap
            if i < j:
                A[i], A[j] = A[j], A[i]

        return A