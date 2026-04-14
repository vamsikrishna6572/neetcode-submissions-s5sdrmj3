class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        product=1
        for i in range(0,n):
            ans.append([product])
            product*=nums[i]
        product=1
        for i in range(n-1,-1,-1):
            ans[i].append(product)
            product*=nums[i]
        
        for i in range(0,n):
            a=ans[i][0]*ans[i][1]
            ans.append(a)
        return ans[n:]
            



        




