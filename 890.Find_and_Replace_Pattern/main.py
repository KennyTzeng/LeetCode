import string

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        l_chars = string.ascii_lowercase

        # pattern conversion
        target_pattern = ""
        bitmap = []
        for char in pattern:
            if char not in bitmap:
                bitmap.append(char)
            target_pattern += l_chars[bitmap.index(char)]

        # words conversion
        convert_strings = []
        for word in words:
            convert_string = ""
            bitmap = []
            for char in word:
                if char not in bitmap:
                    bitmap.append(char)
                convert_string += l_chars[bitmap.index(char)]
            convert_strings.append(convert_string)

        # compare pattern and return
        match_words = []
        for index in range(len(convert_strings)):
            if convert_strings[index] == target_pattern:
                match_words.append(words[index])

        return match_words
        