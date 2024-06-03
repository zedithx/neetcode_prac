from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for num in nums:
            # if number is start of a seq
            if (num - 1) not in num_set:
                length = 1
                while (num+length) in num_set:
                    length += 1
                max_length = max(max_length, length)
        return max_length