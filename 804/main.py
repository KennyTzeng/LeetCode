import string

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        l_chars = string.ascii_lowercase        
        morse_chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_words = []

        for word in words:
            morse_word = ""
            for char in word:
                morse_word += morse_chars[l_chars.index(char)]
            if morse_word not in morse_words:
                morse_words.append(morse_word)

        return len(morse_words)
