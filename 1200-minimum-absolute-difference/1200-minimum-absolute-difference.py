class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        nb=float("inf")
        ll=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<=nb:
                nb=arr[i+1]-arr[i]
                ll.append([arr[i],arr[i+1]])
        ll1=[]
        for i in ll:
            if i[1]-i[0]==nb:
                ll1.append(i)
        return ll1 

                    
                
