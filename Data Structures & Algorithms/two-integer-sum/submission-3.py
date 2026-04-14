class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,num in enumerate(nums):
            a[num]=i
        for i,n in enumerate(nums):
            curr=target-n
            if (curr in a and a[curr]!=i):
                return [i,a[curr]]
        