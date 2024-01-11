def alternative(input):
    i = 0
    j = len(input) - 1
    new_string = ''

    while j > i:
        new_string = new_string + input[i] + input[j]
        i = i + 1
        j = j - 1
    return new_string

print(alternative("abcdef"))
print(alternative("abcde"))
print(alternative("abcdefg"))