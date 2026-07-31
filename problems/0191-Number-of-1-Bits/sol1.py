# ==========================================================
# 191. Number of 1 Bits
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 0 ms (Beats 100%)
# Memory     : 19.3 MB (Beats 55%)
# Link       : https://leetcode.com/problems/number-of-1-bits/
# ==========================================================

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count+=1
            n = n & (n-1)


        
        return count
        
        