#3:38 - 3:44 = 7 mins

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''

        length1 = len(word1)
        length2 = len(word2)

        i = 0
        while True:
            if i<length1:
                output += word1[i]
            if i<length2:
                output += word2[i]  
            
            if i>=length1 and i>=length2:
                break
            i+=1

        return output
            