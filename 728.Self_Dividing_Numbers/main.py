class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            if self.check(i):
                result.append(i)
        return result
    
    def check(self, number):
        temp = number
        while(temp > 0):
            if(temp % 10 == 0):
                return False
            if(number % (temp%10) != 0):
                return False
            temp /= 10
            temp = int(temp)
        return True