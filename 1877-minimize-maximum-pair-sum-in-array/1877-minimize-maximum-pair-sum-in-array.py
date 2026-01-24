class Solution(object):    
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        ll=[]
        while i<j:
            ll.append(nums[i]+nums[j])
            i+=1
            j-=1
        
        return max(ll)