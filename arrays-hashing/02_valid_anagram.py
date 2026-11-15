"""
Valid Anagram (Easy)
Pattern: Arrays & Hashing - frequency count with dicts
Time: O(n) | Space: O(1) (max 26 lowercase letters)
Notes: length check first for early exit. Return the comparison directly, no if/else.
Idiomatic alt: Counter from collections.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm1 = {}
        hm2 = {}

        for i in range(len(s)):
            hm1[s[i]] = hm1.get(s[i], 0) + 1
            hm2[t[i]] = hm2.get(t[i], 0) + 1

        return hm1 == hm2
