class Solution:
    # @param A : string
    # @return a list of strings
    def __init__(self):
        self.result = []
        
    def letterCombinations(self, A):
        buttons = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
            
        self.backtrack(buttons, A, [''])
        return self.result
    
    def backtrack(self, buttons, A, current_letters):
        if not A:
            self.result.append(''.join(current_letters))
            return
        
        current_letters = [x+y for x in current_letters for y in buttons[A[0]]]
        
        for current_letter in current_letters:
            self.backtrack(buttons,A[1:],[current_letter])                