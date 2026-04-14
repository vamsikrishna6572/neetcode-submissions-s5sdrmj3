class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        if(n!=len(t)):
            return False
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        for i in range(n):
            if(s[i]!=t[i]):
                return False
        return True