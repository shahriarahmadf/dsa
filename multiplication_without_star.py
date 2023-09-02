def multiplication_without_star(a,b,multiplicator=None):

    if multiplicator == None:
        # swap a and b, when the function runs first time, for optimization
        if b>a:
            a = a+b
            b = a-b
            a = a-b
        multiplicator = a

    # base case
    if b == 1:
        return a
    # recursive case
    else:
        a += multiplicator
        return multiplication_without_star(a,b-1,multiplicator)
    
print(multiplication_without_star(3,7))