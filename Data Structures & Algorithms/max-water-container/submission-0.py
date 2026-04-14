class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=0
        for i in range(0,n-1):

            for j in range(i+1,n):
                temp=min(heights[i],heights[j])*(j-i)
                ans=max(temp,ans)
        return ans
        