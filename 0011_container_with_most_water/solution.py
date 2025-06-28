class Solution:
    def maxArea(self, height: List[int]) -> int:
        li, ri, area = 0, len(height) - 1, 0

        while li < ri:
            area = max((min(height[li], height[ri]) * (ri - li)), area)
            if height[li] > height[ri]:
                ri -= 1
            else:
                li += 1

        return area
