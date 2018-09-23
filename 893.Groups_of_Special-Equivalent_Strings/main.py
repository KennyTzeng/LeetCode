class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ret = list()

        for string in A:
            list_odd = list()
            list_even = list()
            for index in range(len(string)):
                if index % 2:
                    list_odd.append(string[index])
                else:
                    list_even.append(string[index])
            
            temp = list()
            list_odd.sort()
            list_even.sort()
            temp.append(list_odd)
            temp.append(list_even)
            if temp not in ret:
                ret.append(temp)
        
        return len(ret)