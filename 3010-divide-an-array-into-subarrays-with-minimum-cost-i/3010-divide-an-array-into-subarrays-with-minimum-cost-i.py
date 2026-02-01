class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nb=nums[0]
        nums=nums[1::]
        nums.sort()
        return nb+nums[0]+nums[1]