class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        s = ''
        spacer = False
        for word in words:
            if spacer == False:
                s += word
                spacer = True
            else:
                s += ' '
                s += word
        return s
