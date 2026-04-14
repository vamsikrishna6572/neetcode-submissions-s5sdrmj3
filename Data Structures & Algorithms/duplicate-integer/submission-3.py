class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Set=set()
        for i in nums:
            if(i not in Set):
                Set.add(i)
            else:
                return True
        return False
        