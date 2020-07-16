class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        if not len(nums) or r * c != len(nums) * len(nums[0]) or (r == len(nums) and c == len(nums[0])):
            return nums
        
        res = []
        temp = []
        count = 0
        for row in nums:
            for num in row:
               temp.append(num)
               count += 1
               if count == c:
                   res.append(temp)
                   count = 0
                   temp = []

        return res
        