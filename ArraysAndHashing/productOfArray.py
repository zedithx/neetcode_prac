from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time Without division operator
        # product[i] is product of all numbers except nums[i]
        # Each product is guaranteed to fit in a 32-bit integer.
        num_dict = {}
        resp_list = []
        for i, num in enumerate(nums):
            num_dict[i] = num
        for i in range(len(nums)):
            temp_store = list(num_dict.keys())
            temp_store.pop(i)
            result = 1
            for element in temp_store:
                result *= num_dict[element]
            resp_list.append(result)
        return resp_list

print(Solution().productExceptSelf([1,2,4,6]))