from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            anagram_dict[sorted_word].append(s)
        return [value for value in anagram_dict.values()]