class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # converting all to lower case
        s = s.lower()

        # new string where only letters and number digits will be included 
        s_new = ''

        # loop through the original string to get s_new 
        for x in s:
            if (x >= 'a' and x <= 'z' or x>='0' and x<='9'):
                s_new = s_new + x
        
        # compare first with last, then second with second last, ... until middle element
        for i in range(0,(len(s_new)//2)):
            if (s_new[i] != s_new[(len(s_new)-1-i)]):
                return False
        return True     

        