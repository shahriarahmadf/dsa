class Solution:
    
    def divide_spaces(self, totalSpaces, divideInto,lastLine=False):          
        output = []
        if divideInto == 0:
            return totalSpaces
        if lastLine == True:
            for i in range(divideInto):
                output.append(1)
            output.append(totalSpaces-divideInto)
            return output

        quotient = totalSpaces // divideInto
        output = [quotient] * divideInto
        
        rem = totalSpaces % divideInto
        index = 0
        for i in range(1,rem+1):
            output[index] += 1
            index += 1
        return output
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        currentWidth = 0
        for word in words:
            if currentWidth + len(word) + len(line) <= maxWidth:
                line.append(word)
                currentWidth += len(word)
            else:
                lines.append(line)
                line = []
                currentWidth = 0
                if currentWidth + len(word) + (len(line)-1) <= maxWidth:
                    line.append(word)
                    currentWidth += len(word)

        lines.append(line)

        final_output = []
        for line_no,line in enumerate(lines):
            char_len = sum(len(element) for element in line)
            word_len = len(line)
            spaces = maxWidth-char_len
            if word_len-1 != 0:
                if line_no == len(lines)-1:
                    spaces = self.divide_spaces(maxWidth-char_len,word_len-1,lastLine=True)
                else:
                    spaces = self.divide_spaces(maxWidth-char_len,word_len-1)
            spaces_index = 0
            line_str = ''
            for word in line:
                line_str += word
                if spaces is not None:
                    if type(spaces) == int:
                        for i in range(spaces):
                            line_str += ' '
                    elif spaces_index < len(spaces):
                        for i in range(spaces[spaces_index]):
                            line_str += ' '
                        spaces_index += 1

            final_output.append(line_str)
            line_str = ''
        return final_output