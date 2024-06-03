from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for str in strs:
            enc_str += f"{len(str)}#{str}"
        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_list = []
        i = 0
        while i < len(s):
            # j is my end tracker while i is my start tracker
            j = i
            while s[j] != "#":
                j += 1
            # j will stop at whr "#" is
            length = int(s[i:j])
            # shift left pointer to start of word
            i = j + 1
            # shift right pointer to end of word
            j += length + 1
            dec_list.append(s[i:j])
            i = j
        return dec_list

print(Solution().encode(["neet","code","love","you"]))
print(Solution().decode("4#neet4#code4#love3#you"))