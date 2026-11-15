"""
Two Sum (Easy)
Pattern: Arrays & Hashing - complement lookup with dict {value: index}
Time: O(n) | Space: O(n)
Notes: check the complement BEFORE storing the current num, so a number never pairs with itself.
Problem guarantees exactly one answer, so return on first match. Brute force is O(n^2).
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_nums = {}

        for i, num in enumerate(nums):
            find = target - num
            if find in seen_nums:
                return [seen_nums[find], i]
            seen_nums[num] = i
