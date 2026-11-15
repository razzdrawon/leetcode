"""
Contains Duplicate (Easy)
Pattern: Arrays & Hashing - "have I seen this before?" -> hash set
Time: O(n) | Space: O(n)
Notes: early exit on first duplicate. Alt: sort + compare neighbors, O(n log n) time, O(1) extra space.
"""
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
