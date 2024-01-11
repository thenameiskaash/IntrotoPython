#O(2^n) basically a reflection of O(logn) over a linear axis
#Commonly used in Recursion

# Recursion, tree height n, two branches
def recursion(i, num):
    if i == len(num):
        return 0
    branch = recursion(i + 1, num)
    branch = recursion(i + 2, num)

#2 is a constant c, can change the constant which will increase the time 
#c branches, where c is sometimes n
def recrusion(i, num, c):
    if i == len(num):
        return 0
    for j in range(i, i + c):
        branch = recrusion(j + 1, num) 