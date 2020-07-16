class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        ret = ""
        for letter in S:
            ret += letter * T.count(letter)
        for letter in T:
            if letter not in S:
                ret += letter

        return ret 