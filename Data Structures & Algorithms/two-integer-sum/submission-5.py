class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        Dict=dict()
        for i in range(len(nums)):
            if((target-nums[i]) in Dict):
                ans.append(Dict[target-nums[i]])
                ans.append(i) 
            else:
                Dict[nums[i]]=i
        return ans
        
        



        