price = 7.5
with_tax = price * 1.09
print(f"Base price ${price:.2f} and with tax ${with_tax:.2f}")
print("Base price ${:.2f} and with tax ${:.2f}".format(price, with_tax))

def celsius(x):
    return (x-32)*5/9

for x in range(0, 100, 10):
    print(f"{x:>3} F | {celsius(x):>6.2f} C") 
# The ">" operator is used to align text to the right at number of spaces 
# The expression {:>3.2f} would align the text three spaces to the right, as well as specify a float 
# number with two decimal places. 
