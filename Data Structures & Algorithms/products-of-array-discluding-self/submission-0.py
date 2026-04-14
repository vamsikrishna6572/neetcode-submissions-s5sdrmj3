class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(0,n):
            product=1
            for j in range(0,n):
                if (j==i):
                    continue

                else:
                    product*=nums[j]
            ans.append(product)
        return ans



        