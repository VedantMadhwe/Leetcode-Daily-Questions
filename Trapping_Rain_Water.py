class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0 for i in range(n)]
        right_max = [0 for i in range(n)]
        water = 0
        maxi = height[0]
        for i in range(n):
            maxi = max(maxi,height[i])
            left_max[i] = maxi

        maxi = height[-1]
        for i in range(n-1,-1,-1):
            maxi = max(maxi,height[i])
            right_max[i] = maxi
        for i in range(n):
            curr_water = min(left_max[i],right_max[i]) - height[i]
            water+=curr_water

        return water 
        

