# Find the maximum number in the list without built in function

#l = [1, 4, 5, 3, 2, 0, -1]

def maximum_num(l):
    max = 0 
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
    return max

def bubble_sort(l):
    increase = 0
    while increase < len(l):
        for i in range(1, len(l)):
            if l[i-1] > l[i]:
                l[i-1], l[i] = l[i], l[i-1]
        increase += 1
    return l

def anotherway(l):
    for i in range(0, len(l)-1):
        for j in range(1, len(l)):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
    return l

lag = [1, 4, 5, 3, 8, 2, 0, -1, -4]
print(bubble_sort(lag))
print(anotherway(lag))