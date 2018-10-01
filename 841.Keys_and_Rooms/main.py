class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        locks = [1] + [0] * (len(rooms) - 1)
        keys = set()

        for key in rooms[0]:
            keys.add(key)
        found = True

        while found:
            found = False
            for i in range(len(rooms)):
                if locks[i] == 0:
                    if i in keys:
                        locks[i] = 1
                        for key in rooms[i]:
                            keys.add(key)
                        found = True

        if 0 in locks:
            return False
        else:
            return True