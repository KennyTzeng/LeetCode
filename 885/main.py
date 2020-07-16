class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        order = [[r0,c0]]

        r = r0
        c = c0
        step = 1
        while len(order) < R*C:
            # go east
            for i in range(step):
                c += 1
                if 0 <= r < R and 0 <= c < C:
                    order.append([r,c])
            # go south
            for i in range(step):
                r += 1
                if 0 <= r < R and 0 <= c < C:
                    order.append([r,c])
            step += 1
            # go west
            for i in range(step):
                c -= 1
                if 0 <= r < R and 0 <= c < C:
                    order.append([r,c])
            # go north
            for i in range(step):
                r -= 1
                if 0 <= r < R and 0 <= c < C:
                    order.append([r,c])
            step += 1

        return order
