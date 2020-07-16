class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        min_A, max_A = min(A), max(A)
        if max_A - min_A > K * 2:
            return max_A - min_A - K * 2
        else:
            return 0