"""
Problem: Concatenation of array
Difficulty: Easy
Topic: Array
Link: https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
"""


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
