#12:40~12:53 = 13 mins

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_indices = []
        vowels = []

        for key,value in enumerate(s):
            if value in ['a','e','i','o','u','A','E','I','O','U']:
                vowel_indices.append(key)
                vowels.append(value)

        if len(vowels) == 0:
            return s
        print(vowels)
        vowels_reversed_s = ''
        i = 0
        for key,value in enumerate(s):
            if len(vowels) != 0 and key == vowel_indices[i]:
                vowels_reversed_s += vowels[-1]
                vowels.pop()
                i += 1
            else:
                vowels_reversed_s += value
        
        return vowels_reversed_s