class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
                if d[i]==k:
                    return i
                    break
        return -1
