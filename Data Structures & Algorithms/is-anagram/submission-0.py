class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        n=len(s)
        m=len(t)
        if(n!=m):
            return False
        for i in range(n):
            if(s[i] in dict):
                dict[s[i]]=dict[s[i]]+1
            else:
                dict[s[i]]=1
            if(t[i]in dict):
                dict[t[i]]=dict[t[i]]-1
            else:
                dict[t[i]]=-1
        for i in dict:
            if(dict[i]>0):
                return False
        return True