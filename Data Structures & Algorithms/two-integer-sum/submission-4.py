class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,j in enumerate(nums):
            if(target-j in a and i!=a[target-j]):
                return [a[target-j],i]
            else:
                a[j]=i