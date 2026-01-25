class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        nb=float("inf")
        if k==1:
            return 0      
        for i in range(len(nums)-k+1):
            if nums[i+k-1]-nums[i]<nb:
                nb=nums[i+k-1]-nums[i]
        return nb 