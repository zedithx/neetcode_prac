from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        num_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
        return list(num_dict.keys())[:k]

print(Solution().topKFrequent([1,1,2,2,3], 2))
print(Solution().topKFrequent([1,2,2,3,3,3], 2))