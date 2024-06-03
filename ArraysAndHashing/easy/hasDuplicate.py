from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for num in nums:
            if num not in numdict.keys():
                numdict[num] = True
            else:
                return True
        return False


assert(Solution().hasDuplicate([1,2,3,3]))
assert(not Solution().hasDuplicate([1,2,3,4]))

