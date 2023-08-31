def integer_to_binary(integer):
    binary = str('')

    while(integer >= 1):
        rem = integer % 2
        integer = integer // 2
        binary = str(rem) + binary
    return binary

print(integer_to_binary(47))
print(integer_to_binary(341))