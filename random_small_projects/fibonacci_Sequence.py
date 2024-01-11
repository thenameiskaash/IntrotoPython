def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        total = fibonacci(n-1) + fibonacci(n-2)
        return total
    
x = int(input("Enter a positional value: "))
ans = fibonacci(x)
print(f"The given position {x} under the fibonacci sequence is {ans}")