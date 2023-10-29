class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_array = s.split()
        return len(s_array[-1])
    
#Alternate solution without using split function

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ''
        for x in s:
            if x == ' ':
                if word != '':
                    words.append(word)
                    word = ''
            else:
                word += x
        if word != '':
            words.append(word)
            
        return len(words[-1])