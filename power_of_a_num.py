class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1
        # recursive case
        if n < 0:
            return (1/self.myPow(x,-n))
        if n % 2 == 0:
            p = self.myPow(x,n/2)
            return p*p
        else:
            return x * self.myPow(x,n-1)