class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        flatten = [num for row in nums for num in row]

        if not len(flatten) or r * c != len(flatten) or (r == len(nums) and c == len(nums[0])):
            return nums
        
        return [flatten[i*c:i*c+c] for i in range(r)]
        