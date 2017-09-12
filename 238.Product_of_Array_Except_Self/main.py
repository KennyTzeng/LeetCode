class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = [1]
        product *= len(nums)
        
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            product[i] *= temp
            
        temp = 1
        for j in range(len(nums)-2, -1, -1):
            temp *= nums[j+1]
            product[j] *= temp
        
        return product
            