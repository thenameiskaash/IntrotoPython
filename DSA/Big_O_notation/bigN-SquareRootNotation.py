# Get all factors of n
import math
n = 12
factors = set()
for i in range(1, int(math.sqrt(n)) + 1):
               if n % 2 == 0:
                       factors.add(i)
                       factors.add(n // i)  
print(factors)