def is_palindrome_rec(text):

    # base case
    if len(text) <= 1:
        return True

    # recursive case
    if text[0] == text[-1]:
        return is_palindrome_rec(text[1:-1])
    else:
        return False
    
print(is_palindrome_rec('madam'))