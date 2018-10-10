import string

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        S = list(S)
        # start
        s = 0
        # end
        e = len(S) - 1

        while s < e:
            while S[s] not in string.ascii_letters and s < len(S) - 1:
                s += 1
            while S[e] not in string.ascii_letters and e > 0:
                e -= 1
            if s < e:
                S[s], S[e] = S[e], S[s]
                s += 1
                e -= 1
        
        return ''.join(S)
