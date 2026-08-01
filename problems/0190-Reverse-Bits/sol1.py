# ==========================================================
# 190. Reverse Bits
# Difficulty : Easy
# Language   : Python
# Solution   : #1
# Runtime    : 39 ms (Beats 90%)
# Memory     : 19.3 MB (Beats 30%)
# Link       : https://leetcode.com/problems/reverse-bits/
# ==========================================================

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n & 1      # Get last bit
            ans <<= 1        # Make space in answer
            ans |= bit       # Add the bit
            n >>= 1          # Remove last bit from n

        return ans
        