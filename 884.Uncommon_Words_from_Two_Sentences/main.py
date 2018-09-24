class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        temp = dict()
        for word in A.split(' ') + B.split(' '):
            if word in temp:
                temp[word] += 1
            else:
                temp[word] = 1

        ret = list()
        for key in temp.keys():
            if temp[key] == 1:
                ret.append(key)
        
        return ret