def string_to_integer(S):
    if len(S) <= 1:
        return (ord(S[0]) - 48)
    else:

        return (ord(S[0]) - 48) * pow(10,len(S) -1) + string_to_integer(S[1:])


# Testing
print(string_to_integer('13531'))