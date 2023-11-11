# 18 mins
from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '' or s is None or numRows == 0 or numRows == 1:
            return s
        rows = defaultdict(str)

        current_row = 1
        direction = True # true means downward false means upward

        for letter in s:
            rows[current_row] += letter

            if direction == True and current_row == numRows:
                direction = False
            elif direction == False and current_row == 1:
                direction = True
            
            if direction == True:
                current_row += 1
            else:
                current_row -= 1
        
        s = ''
        for row in rows.values():
            s += row
        return s