class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        distance = 0
        for bit in bin(x ^ y)[2:]:
            if(bit == "1"):
                distance += 1
        return distance