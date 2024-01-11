import numpy as np
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(len(matrix))
print(matrix)

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

print(gcd(20,10))

numbers = [i for i in range(1001)]
print(numbers)

even = [i for i in range(1, 1001) if i % 2 == 0]
print(even)