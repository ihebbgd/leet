class Solution(object):

    def pref(self,ch,ch1):
        pref=""
        for i,j in zip(ch,ch1):
            if i==j:
                pref+=i
            else:
                break
        return pref
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ch=strs[0]
        for i in range(1,len(strs)):
            ch=self.pref(ch,strs[i])
            if ch=="":
                return ""
        return ch
        