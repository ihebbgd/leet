class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumodd=n*n
        sumeven=n*(n+1)
        while sumodd:
            temp = sumodd
            sumodd = sumeven % sumodd
            sumeven = temp
        return sumeven