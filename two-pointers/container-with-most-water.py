class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)
        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            if curr_area > max_area:
                max_area = curr_area

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1


        return max_area
