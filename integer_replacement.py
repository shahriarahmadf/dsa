class Solution:
    def integerReplacement(self, n: int) -> int:
        import math
        count = 0
        while(n!=1):
            if n % 2 != 0:
                count = count + 1
                return count + min(self.integerReplacement(n+1),self.integerReplacement(n-1))
            n = n / 2
            count = count + 1
        return count