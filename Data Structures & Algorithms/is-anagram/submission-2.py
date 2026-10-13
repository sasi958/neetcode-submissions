class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        from collections import Counter

        # Count frequency of characters
        count_s = Counter(s)
        count_t = Counter(t)

        # Directly check if frequency maps are identical
        is_equal = count_s == count_t

        return is_equal
        