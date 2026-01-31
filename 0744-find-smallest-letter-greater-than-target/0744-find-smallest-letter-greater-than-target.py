class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ll=list(letters)
        if target not in letters:
            ll.append(target)
        ll.sort()
        index=len(ll)-ll[::-1].index(target)-1
        if index<len(ll)-1:
            return ll[index+1]
        return letters[0]