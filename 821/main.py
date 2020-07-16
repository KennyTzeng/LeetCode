class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_pos = []
        dis = []
        for index in range(len(S)):
            if S[index] == C:
                c_pos.append(index)

        for index in range(len(S)):
            dis.append(min(abs(c_index - index) for c_index in c_pos))

        return dis
