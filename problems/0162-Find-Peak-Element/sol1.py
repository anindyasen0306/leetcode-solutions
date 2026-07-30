# ==========================================================
# 162. Find Peak Element
# Difficulty : Medium
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.3 MB (Beats 38%)
# Link       : https://leetcode.com/problems/find-peak-element/
# ==========================================================

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = max(nums)
        

        for i in range(len(nums)):
            if nums[i] == n:
                return i
        