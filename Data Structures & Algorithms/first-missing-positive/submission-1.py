class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp={}
        for i in nums:
            temp[i]=1
        maximum=0
        for i in temp:
            maximum=max(i,maximum)
        count=1
        while(count<=maximum):
            if count not in temp:
                return count
            else:
                count+=1
        return count




        