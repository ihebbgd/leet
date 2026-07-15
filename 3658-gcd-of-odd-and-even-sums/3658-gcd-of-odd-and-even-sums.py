class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumodd=1
        sumeven=2
        for i in range(1,n):
            nb=1+i*2
            sumodd+=nb
            nb=2+i*2
            sumeven+=nb
        for i in range(1,sumeven//2+1):
            if(sumodd%i==0 and sumeven%i==0):
                gcd=i
        return gcd