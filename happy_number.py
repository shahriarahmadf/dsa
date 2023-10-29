class Solution:
    def __init__(self):
        self.history = []
    
    def isHappy(self, n: int) -> bool:
        if n in self.history:
            return False
        self.history.append(n)

        total = 0
        while n>0:
            rem = n%10
            n = n//10
            total += rem**2
        
        if total == 1:
            return True
        else:
            n = total
            return self.isHappy(n)
        