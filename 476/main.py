class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        # for example: 101(2) ^ 111(2) = 010(2)
        return num ^ int('1' * (len(bin(num)) - 2), 2) 