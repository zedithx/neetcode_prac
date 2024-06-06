from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        To dictate the amount of water the bars can hold,
        it is determined by the min of the two bars multiplied
        by the number of index they are apart
        """
        l,r = 0, len(heights) - 1
        res = 0
        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return res

