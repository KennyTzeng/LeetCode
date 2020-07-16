class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        for index in range(1,len(A)):
            if(A[index] > A[index-1] and A[index] > A[index+1]):
                return index