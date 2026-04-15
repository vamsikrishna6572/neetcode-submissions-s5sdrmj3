class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        m=len(strs)
        if(m==0):
            return ans
        n=len(strs[0])
        for i in range(n):
            for j in range(1,m):
                if(i>=len(strs[j]) or strs[0][i]!=strs[j][i]):
                    return ans
            ans+=strs[0][i]
        return ans
        