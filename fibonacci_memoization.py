class Solution:
    def __init__(self):
        # adding memo : initializing with base case
        self.memo = {
            0 : 0,
            1 : 1
        }
    
    def fib(self, n: int) -> int:

        # recursive case but also saving in memo
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        
        return self.memo[n]
        
         