class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        index_cache = {}
        for i in range(len(nums2)):
            index_cache[nums2[i]] = i

        res = []
        found = False
        for num in nums1:
            found = False
            for i in range(index_cache[num]+1, len(nums2)):
                if nums2[i] > num:
                    res.append(nums2[i])
                    found = True
                    break

            if not found:
                res.append(-1)

        return res
