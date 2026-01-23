class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ch=""
        x1=x
        if x<0:
            return False
        if x==0:
            return True
        while x>0:
            ch+=str(x%10)
            x=x//10
        return int(ch)==x1

        