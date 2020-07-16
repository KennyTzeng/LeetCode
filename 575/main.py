class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = set(candies)
        
        if len(kinds) >= len(candies) / 2:
            return int(len(candies) / 2)
        else:
            return len(kinds)