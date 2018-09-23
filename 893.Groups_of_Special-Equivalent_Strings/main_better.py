class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = set()

        for string in A:
            list_odd = list(string[::2])
            list_even = list(string[1::2])
            list_odd.sort()
            list_even.sort()
            temp = ''.join(list_odd) + ''.join(list_even)
            count.add(temp)
        
        return len(count)