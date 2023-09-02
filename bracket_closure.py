def bracket_closure(s):

    req_ending_brackets = []
    pointer = 0

    for x in s:
        if x=='(':
            req_ending_brackets.append(')')
        elif x=='{':
            req_ending_brackets.append('}')
        elif x=='[':
            req_ending_brackets.append(']')

        elif x == ')' or x == '}' or x == ']':
            if req_ending_brackets[pointer] == x:
                req_ending_brackets[pointer] = 0
                pointer += 1
            else:
                break
 
    if (pointer == len(req_ending_brackets)):
        return True
    else:
        return False
    
print(bracket_closure('(()'))