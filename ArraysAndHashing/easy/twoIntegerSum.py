from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = {}
        for i in range(len(nums)):
            if nums[i] not in target_dict:
                target_dict[target-nums[i]] = i
            else:
                return [target_dict[nums[i]], i]


assert(Solution().twoSum([3,4,5,6], 7)) == [0,1]
assert(Solution().twoSum([4,5,6], 10)) == [0,2]
assert(Solution().twoSum([5,5], 10)) == [0,1]

