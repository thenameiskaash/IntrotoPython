results = []
for x in range(1,11):
    results.append(x*7)
print(results)

result_1 = [x*7 for x in range(1,11)]
print(result_1)

def odd_numbers(numbers):
    return [x for x in range(0, numbers+1) if x % 2 != 0]
    
print(odd_numbers(5))

#Converting the list of lowercase strings using List comprehension
strings = ['SonJA', 'niChOLAs', 'KyLIe']
lower_string = [x.lower() for x in strings]
print("Lower Strings : ", lower_string)

# Formating the names properly 
formated_strings = [x[0].upper() + x[1:].lower() for x in strings]
capitalize = [x[0].capitalize for x in strings]
print("Formated Strings : ", formated_strings)

# Dict Comprehension - key expression : val expression
d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
flipped = {v:k for (k, v) in d.items()}
print("Flipped: ", flipped)