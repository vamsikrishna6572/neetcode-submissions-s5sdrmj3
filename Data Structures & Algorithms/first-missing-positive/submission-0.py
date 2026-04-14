class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count=1
        while(count<(2**31)):
            if(count not in nums):
                return count
            else:
                count+=1
        return count
        