from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # they are already sorted in ascending
        # means I can use two pointer
        # if value less than target, shift lp
        # if value more than target, shift rp
        # return [lp, rp]
        # take note indexed - 1!
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            sum_numbers = numbers[lp] + numbers[rp]
            if sum_numbers > target:
                rp -= 1
            elif sum_numbers < target:
                lp += 1
            else:
                # I got the answer
                return [lp + 1, rp + 1]
