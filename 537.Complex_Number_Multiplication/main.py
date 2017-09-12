class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_real = int(a.split("+")[0])
        a_imaginary = int(a.split("+")[1].split("i")[0])
        b_real = int(b.split("+")[0])
        b_imaginary = int(b.split("+")[1].split("i")[0])

        return str(a_real * b_real - a_imaginary * b_imaginary) + "+" +str(a_real * b_imaginary + b_real * a_imaginary) + "i" 