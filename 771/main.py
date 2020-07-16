class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jewel_type = []
        count = 0

        for x in J:
            jewel_type.append(x)

        for y in S:
            if y in jewel_type:
                count += 1

        return count


print(Solution().numJewelsInStones("aA", "aAAbbbb"))