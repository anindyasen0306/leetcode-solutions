# ==========================================================
# 204. Count Primes
# Difficulty : Medium
# Language   : Python
# Solution   : #2
# Runtime    : 1642 ms (Beats 35%)
# Memory     : 58 MB (Beats 43%)
# Link       : https://leetcode.com/problems/count-primes/
# ==========================================================


        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j] = False

        for i in range(2,n):
            if prime[i]:
                count += 1

        return count
        