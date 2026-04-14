class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        visited=[0]*n
        ans=[]
        for i in range(0,n):
            if(visited[i]==0):
                temparr=[]
                temparr.append(strs[i])
                temp={}
                for element in strs[i]:
                    if element in temp:
                        temp[element]+=1
                    else:
                        temp[element]=1
                for j in range(i+1,n):
                    temp1={}
                    if(visited[j]==0):
                        for element in strs[j]:
                            if element in temp1:
                                temp1[element]+=1
                            else:
                                temp1[element]=1
                        if(temp==temp1):
                            temparr.append(strs[j])
                            visited[j]=1
                    else:
                        continue
                ans.append(temparr)
                visited[i]=1
        return ans         