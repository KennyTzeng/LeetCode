class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        counts = [0]
        for i in range(1,num+1):
            counts.append(counts[i >> 1] + (i & 1))
        return counts
