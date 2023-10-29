class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # decimal to binary in string form
        binary = ''
        while n>0:
            binary = str(n % 2) + binary
            n = n // 2
        
        # find the number of 1 bits
        count = 0
        for digit in binary:
            if digit == '1':
                count += 1
        
        return count