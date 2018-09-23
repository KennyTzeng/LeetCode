class Solution(object):
    topRow = {'Q', 'q', 'W', 'w', 'E', 'e', 'R', 'r', 'T', 't', 'Y', 'y', 'U', 'u', 'I', 'i', 'O', 'o', 'P', 'p'}
    middleRow = {'A', 'a', 'S', 's', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l'}
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []

        for word in words:
            rowsInUse = 0

            for letter in word:
                if letter in self.topRow:
                    rowsInUse = rowsInUse | 1
                elif letter in self.middleRow:
                    rowsInUse = rowsInUse | 2
                else:
                    rowsInUse = rowsInUse | 4

            if bin(rowsInUse).count('1') < 2:
                result.append(word)

        return result