class Solution:
    ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """    
        res = []
        for word in words:
            if self.is_same_row(word):
                res.append(word)
        return res
            
    def is_same_row(self, word):
        word = word.lower()

        if word[0] in self.ROWS[0]:
            row = 0
        elif word[0] in self.ROWS[1]:
            row = 1
        elif word[0] in self.ROWS[2]:
            row = 2

        for c in word[1:]:
            if c not in self.ROWS[row]:
                return False
        return True