class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse_x = ''
        for digit in str(x):
            reverse_x = digit + reverse_x

        if int(reverse_x) == x:
            return True
        else:
            False