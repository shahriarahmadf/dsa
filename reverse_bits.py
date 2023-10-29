class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ''

        # get binary representation in reverse way
        while n > 0: 
            rem = n % 2
            binary += str(rem)
            n = n // 2
        
        # refill the zeros
        for i in range(32-len(binary)):
            binary += '0'

        # binary to decimal
        power = len(binary) - 1

        decimal = 0
        for digit in binary:
            if digit == '1':
                decimal += 2**power
            power -= 1

        return decimal

            