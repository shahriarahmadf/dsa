class Solution:
    def isValid(self, s: str) -> bool:
           
        req_ending_brackets = []
        bracket_mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for x in s:
            if x in bracket_mapping.keys():
                req_ending_brackets.append(bracket_mapping[x])
            
            elif x in bracket_mapping.values():
                if len(req_ending_brackets) == 0:
                    return False
                elif req_ending_brackets[-1] == x:
                    del req_ending_brackets[-1]
                else:
                    return False

        if len(req_ending_brackets) == 0:
            return True
        else:
            return False
        