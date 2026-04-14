class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        visited=[0]*n
        res=[]
        for i in range(0,n):
            if(visited[i]==0):
                temp=[]
                temp.append(strs[i])
                for j in range(i+1,n):
                    if(visited[j]==0 and len(strs[j])==len(strs[j])):
                        if(sorted(strs[i])==sorted(strs[j])):
                            temp.append(strs[j])
                            visited[j]=1
                res.append(temp)
                visited[i]=1
        return res
        