class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        dict_T = dict()
        # count how many times every letter occurs
        for letter in T:
            if letter in dict_T:
                dict_T[letter] += 1
            else:
                dict_T[letter] = 1

        # put them in order of S
        ret = ""
        for letter in S:
            if letter in dict_T:
                ret += letter * dict_T[letter]
                del dict_T[letter]

        # concatenate others
        for letter in dict_T:
            ret += letter * dict_T[letter]

        return ret 