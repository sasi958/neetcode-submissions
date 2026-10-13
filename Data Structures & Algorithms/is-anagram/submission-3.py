class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        # from collections import Counter

        # # Count frequency of characters
        # count_s = Counter(s)
        # count_t = Counter(t)

        # # Directly check if frequency maps are identical
        # is_equal = count_s == count_t

        # return is_equal

        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count[ord(char) - ord('a')] -= 1

        # Valid anagram if all counts balance to 0
        is_valid = all(c == 0 for c in count)
        return is_valid