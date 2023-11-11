class Solution:
    def compress(self, chars: List[str]) -> int:
        if chars == []:
            return 0
        current_char = None
        freq = 0
        output = ''
        for char in chars:  
            if current_char is None:
                current_char = char
                freq += 1
            elif char == current_char:
                freq += 1
            else:
                if freq == 1:
                    output = output + current_char
                else:
                    output = output + current_char + str(freq)
                current_char = char
                freq = 1
        if freq == 1:
            output = output + current_char
        else:
            output = output + current_char + str(freq)        
        index = 0
        for i in range(len(chars)):
            if index == len(output):
                break
            chars[i] = output[index]
            index += 1
        return len(output)
