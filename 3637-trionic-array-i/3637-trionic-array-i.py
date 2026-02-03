class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        if n<4:                               #CAS IMPOSSIBLE CAR ON NE PEUT MEME PAS DIVISER EN 3 PARTIE !
            return False                     
        i=1
        while i<n and nums[i]>nums[i-1]:     #CAS OU ON VERIFIE QUE LA 1ERE PARTIE STRICTLY INCREASING
            i+=1
        if i==n or i==1:
            return False                    
        
        while i<n and nums[i]<nums[i-1]:#CAS OU ON VERIFIE QUE LA 2EME PARTIE STRICTLY DECREASING
            i+=1
            if i==n:
                return False             
        
        while i<n and nums[i]>nums[i-1]:#CAS OU ON VERIFIE QUE LA 3EME PARTIE STRICTLY INCREASING
            i+=1
        
        if i==n:
            return True                   #SI ON A ATTEINT N ALORS C'EST VRAI SINON C'EST FAUX                                          #BIG MIND IBGD 
        else:
            return False
        
        
        
            
