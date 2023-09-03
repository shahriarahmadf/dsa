
def isHappy(n: int) -> bool:
    def happy(n,loop=False):
    
        n = str(n)
        total = 0
        for digit in n:
            total = total + int(digit)**2
        
        if loop==False:
            loop = total  
        if total == 1:
            return True
        if loop == n:
            return False
        
        return happy(total,loop)

    return happy(n)

print(isHappy(19))
