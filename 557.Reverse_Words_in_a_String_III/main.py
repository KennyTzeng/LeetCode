class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        reverseWords_str = ""
        temp_str = ""

        for char in s:
            if char != " ":
                temp_str += char
            else:
                reverseWords_str += temp_str[::-1]
                temp_str = ""
                reverseWords_str += " "
        reverseWords_str += temp_str[::-1]

        return reverseWords_str