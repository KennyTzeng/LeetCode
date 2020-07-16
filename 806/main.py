import string

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        new_widths = {}
        for char in string.ascii_lowercase:
            new_widths[char] = widths.pop(0)

        lines_count = 1
        line_width = 0
        for char in S:
            if line_width + new_widths[char] > 100:
                lines_count += 1
                line_width = 0
            line_width += new_widths[char]
        
        return [lines_count, line_width]
                