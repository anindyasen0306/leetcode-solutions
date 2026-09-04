class Solution:
    

    def myPow(self, x: float, n: int) -> float:
        # return x**n
        if n == 1:
            return x

        if n%2 == 0:
            return (x**(n//2))**2

        if n%2 != 0:
            return ((x**(n//2))**2)*x


        