class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            if char not in s_dict.keys():
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        for char in t:
            if char not in t_dict.keys():
                t_dict[char] = 1
            else:
                t_dict[char] += 1
        if s_dict == t_dict:
            return True
        return False

assert(Solution().isAnagram("racecar", "carrace"))
assert(not Solution().isAnagram("jar", "jam"))
