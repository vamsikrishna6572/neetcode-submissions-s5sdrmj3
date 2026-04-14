class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Dict=dict()
        for i in s:
            if(i in Dict):
                Dict[i]=Dict[i]+1
            else:
                Dict[i]=1
        for i in t:
            if(i not in Dict):
                return False
            else:
                if(Dict[i]==1):
                    del Dict[i]
                else:
                    Dict[i]=Dict[i]-1
        if not Dict:
            return True
        else:
            return False
        